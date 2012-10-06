#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_BasicObject.py
# @ Date : 2011-11-09
# @ ModifyHistory :
# @ Remark : 
#==================================================================
class BasicObject:    
    id = -1;
    
    def __init__(self, id = -1):
        self.id = id;
        
    def setID(self, id):
        self.id = id;
        
    def __getID(self):
        return self.id;