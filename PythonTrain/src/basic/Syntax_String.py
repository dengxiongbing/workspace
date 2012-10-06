#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_String.py
# @ Date : 2011-11-17
# @ ModifyHistory :
# @ Remark : 
#==================================================================

if __name__ == '__main__':
    print("字符串创建方式:");
    strTemp = "this is a string of python!"
    print (type(strTemp));
    strTemp = 'this is a string of python!'
    print (type(strTemp));
    strTemp = '''this is a string of python!'''
    print (type(strTemp));
    
    print ("Python 字符串的引号和双引号是相同的:");
    strTemp = 'this \t is a string of python!';
    print (strTemp);
    strTemp = "this \t is a string of python!";
    print (strTemp);
    
    print ("自然字符串:");
    strTemp = r'this \t is a string of python!';
    print (strTemp);
    strTemp = R"this \t is a string of python!";
    print (strTemp);
    
    print ("Unicode字符串:");
    strTemp = '这是一个字符串';
    print (strTemp);
    print (len(strTemp));
    strTemp = U'这是一个字符串';
    print (strTemp);
    print (len(strTemp));
    
    print ("字符串自动连接效果:");
    strTemp = '前面部分'"后面部分"
    print("    " + strTemp);
    
    print("字符串连接之加号:");
    strTemp = "前面部分" + "后面部分";
    print ("   " + strTemp);
    
    print ("访问字符串中的某一个字符:");
    strTemp = "this is a string of python";
    char = strTemp[1];
    print (char);
    print (type(char));
    
    strTemp = "this is a string of python";
    strTemp = strTemp[1:-1];
    print (strTemp);
    print ("字符串重复操作符:");
    strTemp = "python";
    strTemp = strTemp * 3;
    print (strTemp);
    