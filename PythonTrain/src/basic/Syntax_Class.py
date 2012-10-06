#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : Syntax_Class.py
# @ Date : 2011-11-20
# @ ModifyHistory :
# @ Remark : 
#==================================================================

import Syntax_BasicObject;
#
#class ExtendObject:
#    id = -1;
#    
#    def __init__(self, id = -1):
#        self.id = id;
#    
#    def setID(self, id):
#        self.id = id;
#    
#    def log(self):
#        print ("I am in Class ExtendObject!");
#
#class InheritObject(ExtendObject):
#        
#    def __init__(self, id = -1):
#        ExtendObject(id);
#    
#    def log(self):
#        print ("I am in Class InheritObject!");
#        
#    def __test(self, value):
#        self.value = value;
#        print ("12345");
#        
#if __name__ == "__main__":
#    print ("演示实例化外部模块中的类:");
#    obj = Syntax_BasicObject.BasicObject(2);
#    print ("对象的ID为:" + str(obj.id));
##    print ("对象的ID为:" + str(obj.__getID()));
#    print ("演示实例化同一模块中的类:");
#    obj = ExtendObject(10);
#    print ("对象的ID为:" + str(obj.id));
#    
#    obj = InheritObject(20);
#    print ("对象的ID为:" + str(obj.id));
#    obj.log();
#    
##    obj._InheritObject__test(123);
#    obj._test(123);
class SchoolMember:
    '''Represents any school member.'''
    name = None;
    age = None;
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ("Initialized SchoolMember: " + self.name);
    
    def tell(self):
        '''Tell my details.'''
        print ("Name:" + self.name + " Age:" + str(self.age));
    
class Teacher(SchoolMember):
    '''Represents a teacher.'''
        
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age);
        self.salary = salary;
        print ("Initialized Teacher: " + self.name);
    
    def tell(self):
        SchoolMember.tell(self)
        print ("Salary: " + str(self.salary));

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ("Initialized Student: " + self.name);

    def __tell(self):
        SchoolMember.tell(self)
        print ("Marks: " + str(self.marks));

if __name__ == '__main__':
    t = Teacher('Mrs. Shrividya', 40, 30000);
    
    s = Student('Swaroop', 22, 75)
    s._Student__tell();
    members = [t, s]
    for member in members:
        member.tell();