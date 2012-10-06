#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : BaseClass
# @ FileName : BaseClass.py
# @ Date : 2011-11-14
# @ ModifyHistory :
# @ Remark :
#==================================================================

class BaseClass:
    id = None;
    
    def __init__(self, id):
        self.id = id;
        
    def setID(self, id):
        self.id = id;        

    def __getID__(self):
        return self.id;
    
class ChildClass(BaseClass):
    
    def __init__(self, id):
        BaseClass.__init__(self, id);
            
     
if __name__ == '__main__':
    obj = BaseClass(10);
    obj.__getID__();
#    id = obj._BaseClass__getID();
    print (id);
    
#    obj = ChildClass(10);
#    id = obj.getID(10);
#    print (id);