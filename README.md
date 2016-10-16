# my_cmd
> 本工程自定义类似cmd命令输入，支持tab循环查找、上下键浏览历史命令；添加和运行自定义命令

## 工程动机

本人收集了不少的有用的小工具（绿色版无需安装的一些小程序），但每次都要到指定目录找到该文件再运行，相当麻烦；当然可以修改系统环境到path来实现在DOS下输入运行，但这样会污染path，而且输入时无法使用自动补全。有了本工程后可以将自己经常要用到小工具添加到命令列表(无需改动path)，而且可以修改小工具对应的命令名来方便运行时输入(直接修改命令存储的文件)，同时还支持输入时tab循环查找、上下键浏览历史命令等常用功能

## 主要知识点

1. 自定义模糊搜索
2. 接收键盘的输入（字符和非字符）及其显示
3. 模拟控制台输入命令的tab循环查找和上下键浏览历史命令等功能

## 需要的库

+ Python 2.7.10
+ 若要生成windows下运行的exe文件，则需要py2exe-0.6.9，然后运行以下命令即可生成exe(生成文件为./exe/dist/my_cmd.exe):

```dos
python get_exe.py py2exe
```

## 注意

+ 添加命令可以将多个文件拖入my_cmd.exe(windwos系统中)上，即可添加命令，命令名默认为文件名(去除路径和后缀)
+ 可修改存储命令的文件来修改命令及其内容，如修改命令名
+ 若遇到运行后直接退出的情况，可以尝试DOS命令行运行查看错误的原因，错误多半是输入命令的文件格式有问题
+ 退出时若不能正常关闭本应用，可能是使用自定义命令运行的部分程序未关闭（也存在部分程序不关闭也可以正常关闭本应用）
