#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_arithmetic.py
# @ Date : 2011-06-08
# @ ModifyHistory :
# @ Remark : 
#==================================================================

if __name__ == '__main__':
    
    operandBefore = 2;
    operandAfter = 4;
    result = operandBefore + operandAfter;
    print ("result:" + str(result)); 

    result = operandBefore - operandAfter;
    print ("result:" + str(result));

    result = operandBefore * operandAfter;
    print ("result:" + str(result));
    operandBefore = 5
    operandAfter = 2
    result = operandBefore / operandAfter;
    print ("result:" + str(result));

    operandBefore = 4;
    operandAfter = 2.5;
    result = operandBefore / operandAfter;
    print ("result:" + str(result));
    
    result = operandBefore ** operandAfter;
    print ("result:" + str(result));
    
    result = operandBefore % operandAfter;
    print ("result:" + str(result));  
    
    operandBefore = 4;
    operandAfter = 2.5;
    # 取比实际商小的最大整数
    result = operandBefore // operandAfter;
    print ("result:" + str(result));
    
    # 位运算符
    operandBefore = 4;
    operandAfter = 3;
    result = operandBefore << operandAfter;
    print(result);
    
    operandBefore = 4;
    operandAfter = 2;
    result = operandBefore >> operandAfter;
    print(result);
     
    operandBefore = 1;
    operandAfter = 7;
    result = operandBefore & operandAfter;
    print(result);
    
    operandBefore = 1;
    operandAfter = 7;
    result = operandBefore | operandAfter;
    print(result);
    
    operandBefore = 1;
    operandAfter = 7;
    result = operandBefore ^ operandAfter;
    print(result);
    
    operandBefore = 1;
    operandAfter = 255;
    result = ~operandAfter;
    print(result);
    
    # 比较运算
    strTempBefore = "this is a string 1";
    
    strTempAfter = "this is a string 2"
    if(strTempBefore > strTempAfter):
        print("大于");
    elif (strTempBefore < strTempAfter):
        print("小于");
    else:
        print ("等于");
    
    # 演示布尔运算
    bTempBefore = True;
    bTempAfter = False;
    
    bResult = bTempBefore and bTempAfter;
    print (bResult);
    bResult = bTempBefore or bTempAfter;
    print (bResult);
    bResult = not bTempAfter;
    print (bResult);
    
#    float 为什么会被截断
#    字符串或者是对象的比较根据什么来做
#    原码补码反码
#    python 字符串比较时是基于字典序的吗
