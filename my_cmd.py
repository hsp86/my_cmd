#-*- coding: utf-8 -*-

import os,sys,re
from _Getch import _Getch
import config

def search_start(src_list,search_str):
    '''查找src_list中以search_str开始的项，返回找到的个数和list'''
    res_num = 0
    res_list = []
    for x in src_list:
        if x.startswith(search_str) != -1:
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
            res_num = res_num + 1
            res_list.append(x)
    return res_num,res_list

def search_have(src_list,search_str):
    '''查找src_list中包含search_str各字符的项，返回找到的个数和list'''
    res_num = 0
    res_list = []
    search_patt = "*"
    for x in search_str:
        search_patt = search_patt + x + "*"
    pattern = re.compile(search_patt)
    for x in src_list:
        s = pattern.search(file_str)
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

def get_cmd_input():
    '''本函数完成接收用户的输入并返回输入的字符，支持tab搜索已有命令，tab循环显示搜索结果'''
    getch = _Getch()
    st = ""
    search_res = [] # 用于存储搜索结果
    search_res_num = 0 # 搜索到的项数
    display_num = 0 # 用于指示当前tab后显示的搜索结果的索引；当输入一个tab后清0
    ch = getch();
    while ch != "\r": # enter键完成命令输入
        if ch == "\t": # tab键
            if display_num == 0: # 若没搜索过就重新搜索
                search_res_num,search_res = fuzzy_search(src_list,st) # 模糊搜索st的项
            # 显示搜索到的第search_res_num个，并设置到st
            if search_res_num > 0: # 搜索到的结果大于0才重新显示，否则不修改st和显示
                if search_res_num <= display_num:
                    display_num = 0 # 若达到最后一个就回到0重新开始显示
                sys.stdout.write("\b" * len(st)) # 删除原显示字符
                st = search_res[display_num]
                sys.stdout.write(st)
            display_num = display_num + 1 # 自增一，准备下次tab显示的位置，即使没搜索到也自增一，防止下次连续tab再次搜索
        else:
            search_res = [] # 输入非tab后清除之前的搜索结果
            search_res_num = 0
            display_num = 0 # 并且清除显示位置
            # print "\b" + ch, # 这样行末始终有一个空格，改用下面的sys.stdout.write
            if ch == "\b": # 删除键
                sys.stdout.write(ch + " " + "\b") # 删除显示，用空格覆盖要删除的字符
                st = st[0:-1] # 从st中删除最后一个字符
            else:
                sys.stdout.write(ch)
                st = st + ch
        ch = getch()
    # print search_res_num # 显示最后输入的tab键次数
    return st


if __name__ == "__main__":
    # st = sys.argv[0]
    st = get_cmd_input()
    sys.stdout.write("\b" * len(st)) # 删除原显示字符重新显示字符
    print "input:" + st
    fid = os.popen(st)
    print fid.read()
    fid.close()
    print u"按Enter退出"
    ch = raw_input();
