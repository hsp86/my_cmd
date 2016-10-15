#-*- coding: utf-8 -*-

import os,sys,re
import config

my_cmd = ["husipeng","hsp86"]
def init():
    '''初始化命令，从文件中读取并存入各变量'''
    pass

def search_start(src_list,search_str):
    '''查找src_list中以search_str开始的项，返回找到的个数和list'''
    res_num = 0
    res_list = []
    for x in src_list:
        if x.startswith(search_str) == True:
            # print "search_start" # 调试用
            res_num = res_num + 1
            res_list.append(x)
    return res_num,res_list

def search_in(src_list,search_str):
    '''查找src_list中包含search_str的项，返回找到的个数和list'''
    res_num = 0
    res_list = []
    for x in src_list:
        # if x.find(search_str) != -1:
        if search_str in x:
            # print "search_in" # 调试用
            res_num = res_num + 1
            res_list.append(x)
    return res_num,res_list

def search_have(src_list,search_str):
    '''查找src_list中包含search_str各字符的项，返回找到的个数和list'''
    res_num = 0
    res_list = []
    search_patt = ".*"
    for x in search_str:
        search_patt = search_patt + x + ".*"
    pattern = re.compile(search_patt)
    for x in src_list:
        # print "search_have" # 调试用
        s = pattern.search(x)
        if s != None:
            res_num = res_num + 1
            res_list.append(x)
    return res_num,res_list

def fuzzy_search(src_list,search_str):
    '''自定的模糊搜索，返回找到的个数和list'''
    res_num = 0
    res_list = []
    res_num,res_list = search_start(src_list,search_str)
    if res_num == 0: # 若没有search_str开始的项就搜索包含search_str的项
        res_num,res_list = search_in(src_list,search_str)
        if res_num == 0: # 若还没有包含search_str的项就搜索包含search_str中各字符的项
            res_num,res_list = search_have(src_list,search_str)
    return res_num,res_list

def del_display(st):
    '''删除显示字符串st'''
    sys.stdout.write("\b" * len(st)) # 开始，删除原显示字符
    sys.stdout.write(" " * len(st))
    sys.stdout.write("\b" * len(st)) # 结束，删除原显示字符

# 用于存储运行过的命令
cmd_history = ["husipeng","hsp86"]
def get_cmd_input():
    '''本函数完成接收用户的输入并返回输入的字符，支持tab搜索已有命令，tab循环显示搜索结果'''
    from _Getch import _Getch
    getch = _Getch()
    cmd = ""
    search_res = [] # 用于存储搜索结果
    search_res_num = 0 # 搜索到的项数
    display_num = 0 # 用于指示当前tab后显示的搜索结果的索引；当输入一个tab后清0
    sys.stdout.write(config.prompt_header) # 显示提示头
    ch = getch();
    while ch != config.cmd_end: # enter键完成命令输入结束符可在config中配置
        if ch == "\t": # tab键
            if display_num == 0: # 若没搜索过就重新搜索
                search_res_num,search_res = fuzzy_search(my_cmd,cmd) # 模糊搜索cmd的项
            # 显示搜索到的第search_res_num个，并设置到cmd
            if search_res_num > 0: # 搜索到的结果大于0才重新显示，否则不修改cmd和显示
                if search_res_num <= display_num:
                    display_num = 0 # 若达到最后一个就回到0重新开始显示
                del_display(cmd) # 删除原显示字符
                cmd = search_res[display_num] # 更改cmd
                sys.stdout.write(cmd)
            display_num = display_num + 1 # 自增一，准备下次tab显示的位置，即使没搜索到也自增一，防止下次连续tab再次搜索
        else:
            search_res = [] # 输入非tab后清除之前的搜索结果
            search_res_num = 0
            display_num = 0 # 并且清除显示位置
            # print "\b" + ch, # 这样行末始终有一个空格，改用下面的sys.stdout.write
            if ch == "\b": # 删除键
                sys.stdout.write("\b" + " " + "\b") # 删除显示，用空格覆盖要删除的字符
                cmd = cmd[0:-1] # 从cmd中删除最后一个字符
            elif ord(ch) == 224: # 上下左右键
                ch = getch()
                # print ord(ch)
                if ord(ch) == 72: # 上键
                    # print u"上键"
                    if len(cmd_history) > 0: # 有历史命令才能处理
                        cmd_history.insert(0,cmd) # 把当前命令放入命令历史首
                        del_display(cmd) # 清除显示
                        cmd = cmd_history.pop(-1) # 从cmd_history末尾取出前一条历史命令
                        sys.stdout.write(cmd) # 显示前一条历史命令
                elif ord(ch) == 80: # 下键
                    # print u"下键"
                    if len(cmd_history) > 0: # 有历史命令才能处理
                        cmd_history.append(cmd) # 把当前命令放入命令历史尾
                        del_display(cmd) # 清除显示
                        cmd = cmd_history.pop(0) # 从cmd_history首取出相对最旧一条历史命令
                        sys.stdout.write(cmd) # 显示最旧一条历史命令
                # elif ord(ch) == 75: # 左键。暂不处理
                    # print u"左键"
                    # sys.stdout.write("\b")
                # elif ord(ch) == 77: # 右键。暂不处理
                #     print u"右键"
                    # sys.stdout.write(chr(0x27)) # 输入右移ASCII，39(0x27)有错
            else: # 其它按键输出打印并存入cmd
                sys.stdout.write(ch)
                cmd = cmd + ch
        ch = getch()
        # print ord(ch)
    cmd_history.append(cmd) # 存入命令历史尾
    # print search_res_num # 显示最后输入的tab键次数
    print "\n", # 输出换行，方便之后输出其它信息
    return cmd

def disp_msg(msg):
    print msg
    print u"\t输入Enter继续"
    raw_input()

def mycmd_execute(cmd):
    '''当做自定义命令执行'''
    fid = os.popen(cmd)
    print fid.read()
    statu_cod = fid.close()
    if statu_cod != None:
        print u'命令执行失败！'
        return -1
    else:
        return 0

def syscmd_execute(cmd):
    '''当做系统命令执行'''
    fid = os.popen(cmd)
    print fid.read()
    statu_cod = fid.close()
    if statu_cod != None:
        print u'命令执行失败！'
        return -1
    else:
        return 0


if __name__ == "__main__":
    arg_len = len(sys.argv[0])
    if arg_len > 1: # 当输入参数大于1时（如将文件拖到本执行文件执行），就为添加命令到文件
        pass
    else: # 当输入参数为1时表示，直接运行，进行输入命令处理
        cmd = get_cmd_input()
        while cmd != 'quit':
            if mycmd_execute(cmd) != 0: # 如果自定义命令执行失败，即cmd不在自定命令中，则当做系统命令来执行
                syscmd_execute(cmd)
            cmd = get_cmd_input() # 执行后继续输入
        disp_msg(u"退出？")

