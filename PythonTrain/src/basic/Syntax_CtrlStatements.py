#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : 控制结构例子
# @ FileName : Syntax_CtrlStatements.py
# @ Date : 2011-10-30
# @ ModifyHistory :
# @ Remark : 
#==================================================================
def doSomeThing():
    print("execute doSomeThing function!");

def doOtherThing():
    print("execute doOtherThing function!");

def doAnotherThing():
    print("execute doAnotherThing function!");
    
def doSomeThingAfterLoop():
    print("execute doSomeThingAfterLoop function!");
    

if __name__ == '__main__':
    condition = True;
    
    # 演示独立的if语句
    if condition:
        doSomeThing();
    
    # 演示if-else语句
    if condition:
        doSomeThing();
    else:
        doOtherThing();
    
    # 演示if-elif-else语句
    anotherCondition = True;
    if condition:
        doSomeThing();
    elif anotherCondition:
        doOtherThing();
    else:
        doAnotherThing();
        
        
    # 演示三元运算符
    i = 0;
    j = 1;
#    result = i if i < j else j;
    

    # 演示for循环
    iterable = [];
    for iter_var in iterable:
        doSomeThing();
    else:
        doSomeThingAfterLoop();
        
    list = [1, 2, 3];
    for elem in list:
        print(elem);

    for i in range(5):
        print(i);
    
    # 演示while语句
    while condition:
        doSomeThing();
        condition = False;
#        break;
    else:
        doSomeThingAfterLoop();           