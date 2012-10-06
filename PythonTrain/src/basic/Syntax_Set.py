#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_Set.py
# @ Date : 2011-11-15
# @ ModifyHistory :
# @ Remark :
#==================================================================

class BasicObject:    
    id = -1;
    
    def __init__(self):
        id = -1;
        
    def setID(self, id):
        self.id = id;
    

if __name__ == '__main__':  
      
    # 创建Set
    setType = set('abcdef');    
    print (setType);
    
    setType.add('a');
    
    print (setType);