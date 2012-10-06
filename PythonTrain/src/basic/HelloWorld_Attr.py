#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : HelloWorld__name__.py
# @ Date : 2011-06-08
# @ ModifyHistory :
# @ Remark : 
#==================================================================

def log__Name__():
    print(__name__);

if __name__ == '__main__':
    # dir()列出指定模块对象或类的属性
    print(dir());
    log__Name__();
