#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_IO.py
# @ Date : 2011-10-30
# @ ModifyHistory :
# @ Remark : 
#==================================================================

if __name__ == '__main__':
    fileName = "resource/file.txt";
    # file_name是文件路径，支持相对路径和绝对路径
    # 文件打开模式'r', 'w', 'a'分别代表读写和追加还有'U'模式代表通用换行符支持
    # 'r' open for reading (default)
    # 'w' open for writing, truncating the file first
    # 'a' open for writing, appending to the end of the file if it exists
    # 'b' binary mode
    # 't' text mode (default)
    # '+' open a disk file for updating (reading and writing)
    # 'U' universal newline mode (for backwards compatibility; unneeded for new code)
    fileObject = open(fileName, 'rw');
    fileObject = file(fileName, 'r');
    content = fileObject.read();
    print ("file content:\n" + content);
    fileObject.close();
    
    # 此段程序在linux下运行通过 
    fileObject = file(fileName, 'r');
    line = "file content";
    while line:
        line = fileObject.readline();
        print ("file content:\n" + str(line));
    
    content = fileObject.readlines();
    print ("file content:\n" + str(content));
    
    content = "the content for writing!";
    fileObject = file(fileName, 'a');
    fileObject.write(content);
    
    lines = ['\n', "***********\n", "12323456y789\n"];
    fileObject.writelines(lines);
    
    fileObject.close();文件句柄回收！？？
    
    
