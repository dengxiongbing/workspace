#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_List.py
# @ Date : 2011-11-14
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
   
# 创建列表
    print ("使用同类型的元素创建列表:");
    firstObj = BasicObject();
    secondObj = BasicObject();
    list = [firstObj, secondObj];
    print (list);
    list = [1, 2, 3];
    print (list);
    
    print ("使用不同类型的元素创建列表:");
    list = ['a','b', 0, 1, 3];
    print(list); 
       
    print ("获取列表的长度:");
    listLen = len(list);
    print (listLen);
    
    print ("获取列表中的某一个元素:");
    var = list[1];
    print (var);    
    var = list[-1];
    print(var);
    
    print ("往列表中追加元素:");
    print ("追加前的列表元素为:");
    print (list);
    list.append(4);
    print ("追加后的列表元素为:");
    print (list);
    
    print ("往列表中插入元素:");
    print ("插入前的列表元素为:");
    print (list);    
    list.insert(1, 5);
    print ("插入后的列表元素为:");
    print(list);
    # list[2:2] = [6];
    # print (list);

    print ("从列表中删除元素:");
    print ("删除元素前:");
    print (list);
    del list[3];
    print ("删除元素后:");
    print (list);

    print ("删除多个元素前:");
    print (list);   
    del list[1:3];
    print ("删除多个元素后:");
    print (list);
    
    # 遍历里列表
    list = ['a','b', 0, 1, 3];
    print ("遍历列表:");
    for elem in list:
        print(elem);
    list = ['a','b', 0, 1, 3];
    listLen = len(list);
    index = 0;
    while(index < listLen):
        elem = list[index];
        index = index + 1;
                
    print ("提取子列表:");    
    print ("提取前:");
    print (list);
    subList = list[1:];    
    print ("提取后:");
    print(subList);
    
    print ("列表相连:");
    print ("列表相连前:");
    print (list);
    print (subList);
    extendList = list + subList;
    print ("列表相连后:");
    print (extendList);