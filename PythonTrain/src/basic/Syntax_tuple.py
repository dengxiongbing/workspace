#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_tuple.py
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
    # 创建元组
    print ("使用同类型的元素创建元组:");
    firstObj = BasicObject();
    secondObj = BasicObject();
    tuple = (firstObj, secondObj);
    print (tuple);
    tuple = (1, 2, 3);
    print (tuple);
    
    print ("使用不同类型的元素创建元组:");
    tuple = ('a','b', 0, 1, 3);
    print(tuple); 
       
    print ("获取元组的长度:");
    tupleLen = len(tuple);
    print (tupleLen);
    
    print ("获取元组中的某一个元素:");
    var = tuple[1];
    print (var);    
    var = tuple[-1];
    print(var);
    
    print ("往元组中追加元素:");
    print ("追加前的元组元素为:");
    print (tuple);
#    tuple.append(4);
    print ("追加后的元组元素为:");
    print (tuple);
 
    print ("从元组中删除元素:");
    print ("删除元素前:");
    print (tuple);
    del tuple;
    print ("删除元素后:");
    print (tuple);
    
    # 遍历里元组
    tuple = (1, 2, 3);
    print ("遍历元组:");
    for elem in tuple:
        print(elem);
    
    print ("提取子元组:");    
    print ("提取前:");
    print (tuple);
    subtuple = tuple[1:];    
    print ("提取后:");
    print(subtuple);
    
    print ("元组相连:");
    print ("元组相连前:");
    print (tuple);
    print (subtuple);
    extendtuple = tuple + subtuple;
    print ("元组相连后:");
    print (extendtuple);