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

class Demo:
    """Demo Class"""
    name = None;
    value = None;
    
    def __init__(self):
        pass;
    
    def setName(self, name):
        self.name = name;
        
    def setValue(self, value):
        self.value = value;

if __name__ == '__main__':
    content = "***content for testing***";
    print(content);
    
    length = len(content);
    
    lenStr = str(length);
    print (lenStr);
    
    result = type(lenStr);
    print (result);
    result = type(length);
    print(result);
    
#    input = raw_input("请随便输入一个字符串:");
#    print("input value:" + input);
    
    list = range(0, 10, 2);
    print (list);
    
    attrs = dir(Demo);
    print (attrs);
    attrs = dir();
    print (attrs);
    
    content = "123";
    print (type(content));
    value = int(content);
    print (type(value));
    
    file = open("resource/file.txt", "rw");
    content = file.readlines();
    print (content);