#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Demo.py
# @ Date : 2011-11-19
# @ ModifyHistory :
# @ Remark :
#==================================================================
globalData = 10;

def mul(firData, secData):
#    global globalData;
#    print ("global Data:" + str(globalData));
#    globalData = 2;
    return firData * secData * globalData;

if __name__ == '__main__':    
    print(mul(10, 2));