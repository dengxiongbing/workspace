#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_DataType.py
# @ Date : 2011-11-09
# @ ModifyHistory :
# @ Remark : 
#==================================================================

def testNoneType():
    data = None;
    print (data);
    print (str(data) + "");
    print (type(data));

def testBoolType():
    data = False;
    data = True;
    print (data);
  
    data = None;
    if(data):
        print ("the condition is True!");
    else:
        print ("the condition is False!");
    
    data = "replace Boolean";
    if(data):
        print ("the condition is True!");
    else:
        print ("the condition is False!");
        
    data = -1;
    if(data):
        print ("the condition is True!");
    else:
        print ("the condition is False!");
        
def testNumType():
    data = 10;
    print (data);
    print (type(data));
    
    data = 1020948320948209482390482390489204820394820390395804583482340952348327490247921471904;
    print (data);
    print (type(data));
    
    data = 1L
    print (data);
    print (type(data));

    data = 0123;
    print (data);
    print (type(data));

    data = 0x123;
    print (data);
    print (type(data));
    
    data = 1.23;
    print (data);
    print (type(data));
    
    data = 1.23e2;
    print (data);
    print (type(data));
    
def testComplexType():
    data = 4 + 3j;
    print("打印复数:");
    print (data);
    print("打印复数实部:");
    print (data.real);
    print("打印复数实部类型:");    
    print (type(data.real));
    print("打印复数虚部:");
    print (data.imag);
    print("打印复数虚部类型:");
    print (type(data.imag));
    
    data = 3j;
    print("打印仅有虚部的复数:");
    print (data);
    print("打印复数的实部默认值:");
    print (data.real);     

if __name__ == '__main__':
#    testNoneType();
#    testBoolType();
#    testNumType();
    testComplexType();