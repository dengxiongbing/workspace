#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_dict.py
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
    # 创建字典
    print ("使用同类型的元素创建字典:");
    firstObj = BasicObject();
    secondObj = BasicObject();
    dict = {'a':firstObj, "b":secondObj};
    print (dict);
    dict = {1 : 'a', 2 : "b"};
    print (dict);
    
    print ("使用不同类型的元素创建元组:");
    dict = {'a' : 1, 2:firstObj};
    print (dict);
    
    dict = {'a' : 1, 'b' : 2};
          
    print ("获取字典的长度:");
    dictLen = len(dict);
    print (dictLen);
    
    print ("获取字典中的某一个元素:");
#    var = dict[1];
#    print (var);
    var = dict['a'];
    print(var);
    
    print ("往字典中追加元素:");
    print ("追加前的字典元素为:");
    print (dict);
    dict['c'] = 3;
    print ("追加后的字典元素为:");
    print (dict);
 
    print ("从字典中删除元素:");
    print ("删除元素前:");
    print (dict);
    del dict['a'];
    print ("删除元素后:");
    print (dict);
    dict.clear();
    print ("清除元素后:");
    del dict;
    print (dict);
    
    dict = {'a' : 1, 'b' : 2};
    
    # 遍历字典
    print ("遍历字典:");
    for elem in dict.iteritems():
        print (elem[0]);
        print (elem[1]);
    for elem in dict.items():
        print (elem[0]);
        print (elem[1]);

    
    print ("获取所有的key值:");
    print (dict.keys());
    print ("获取所有的value值:");
    print (dict.values());
    
    print ("判断是否存在key值:");    
    print (dict.has_key('a')); 
    