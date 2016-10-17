#-*- coding: utf-8 -*-

# 输入命令显示提示字符
prompt_header = "hsp>"

# 指定存储命令的文件
cmd_file = "cmd.txt"

# 指定结束输入命令的字符
# 如使用windows结束符"\r\n"所以可指定为"\r"
cmd_end = "\r"

# 指定系统目录分割符
separate_char = "\\"
# 后缀分隔符；命令名默认为去除后缀的文件名
suffix_char = "."
# 文件中存储的命令格式为：命令名+以下字符+命令内容
div_char = ";"

# 指定要添加为命令的文件的后缀名。指定为[]则表示所有后缀的文件；
# suffixs无论指定为何值都支持没有后缀的文件或目录
# suffixs = []
suffixs = ["exe","vbs","cmd","bat"]
