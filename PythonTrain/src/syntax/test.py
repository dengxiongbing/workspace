'''
Created on 2011-11-24

@author: xiaodeng
'''
import os;
import sys;

#import testpackage.BaseClass as base;

from testpackage.BaseClass import BaseClass, ChildClass;
if __name__ == '__main__':
    obj = BaseClass(10);
    obj = ChildClass(10);
#    obj = testpackage.BaseClass.BaseClass(10);