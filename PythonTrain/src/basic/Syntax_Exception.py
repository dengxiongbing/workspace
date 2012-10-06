#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : 异常处理
# @ FileName : Syntax_Exception.py
# @ Date : 2011-10-30
# @ ModifyHistory :
# @ Remark : 
#==================================================================

def doSomeThing():
    print("execute doSomeThing function!");

def doExceptThing():
    print("execute doExceptThing function!");

def doAnotherExceptThing():
    print("execute doAnotherExceptThing function!");
    
def doElseThing():
    print("execute else function!");

def doFinallyThing():
    print("execute finally function!");

if __name__ == '__main__':
    try:
        doSomeThing();
#        raise IOError();
#        raise EOFError();
    except (EOFError,IOError), e:
        doExceptThing();
    except Exception, e:
        doAnotherExceptThing();    
    else:
        doElseThing();
    
    try:
        doSomeThing();
#        raise IOError();
        raise EOFError();
    finally:
        doFinallyThing();