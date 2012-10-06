#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : explain the concepts of　python
# @ FileName : HelloWorld.py
# @ Date : 2011-06-08
# @ ModifyHistory :
# @ Remark : 
#==================================================================

if __name__ == '__main__':
    
    #  说明标识符概念
    varName = 1;
    VARNAME = 1;
    _varName = 1;
    _varName1 = 1;
    __varName1 = "a";
    # 1varName = 1;
    
    varName = 1;
    VarName = 2;
    print ("varName:" + str(varName));print ("VarName:" + str(VarName));
    
    if True:
        print ("A new statement!");
        
    # 演示续行符
    varName = "1234\
5678";
    print (varName);
    
    for ch in \
    varName:
        print (ch);