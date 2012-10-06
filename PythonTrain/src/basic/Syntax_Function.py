#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_Function.py
# @ Date : 2011-11-19
# @ ModifyHistory :
# @ Remark :
#==================================================================
globalData = 10;

def add(firData, secData, thirdData):
    var_COMM = "我是普通局部变量!";
    return firData + secData + thirdData;

def sub(firData, secData, thirdData = 0):
    var_ART = "我是文艺局部变量!";
    return firData - secData - thirdData;

# 错误的默认函数定义
#def subError (firData, secData = 0, thirdData):
#    return firData - secData - thirdData;

# 演示变量的作用域
globalData = 10;
def mul(firData, secData):
    global globalData;
    print ("global Data:" + str(globalData));
    globalData = 2;
    return firData * secData * globalData;

def div(firData, secData):
    '''我是这个函数的文档字符串,这个函数实现两个数相除的功能'''
    print (firData / secData);

if __name__ == '__main__':
    # 演示文档字符串
    print ("演示文档字符串:");
    print (div.__doc__);
    fir = 1;
    sec = 2;
    thd = 3;
    
    # 普通的调用
    print("演示普通函数调用:");
    print (add(fir, sec, thd));
    # 错误的调用， 参数个数不对
    # print (add(fir, sec));
    
    # 对有默认参数的函数的调用方式
    print("演示默认参数:");
    print (sub(fir, sec));
    print (sub(fir, sec, thd));
    
    # 关键参数
    print ("演示关键参数:");
    print (sub(secData = sec, firData = fir));
    
    # 变量作用域
    print ("*************演示变量作用域**************");
    print ("全局变量的值为:" + str(globalData));
    globalData = 5;
    print ("全局变量的值为:" + str(globalData));
    fir = 1;
    sec = 2;   
    print (mul(fir, sec)); 
    print (globalData);
    
    # 演示文档字符串
    print ("演示文档字符串:");
    print (div.__doc__);
    
    # 演示注意事项
    print ("演示注意事项:");
#    print (None);
    print (div(1,2));
    
def test():
    pass;