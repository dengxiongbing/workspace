#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent ISD
# @ Desc : update source code
# @ FileName : HelloWorld.py
# @ Date : 2011-06-08
# @ ModifyHistory :
# @ Remark : 
#==================================================================

if __name__ == '__main__':
    print("Hello World!")
    
'''
 1. #!/usr/bin/env python   
         指示系统到环境变量里设置的系统路径下去查找Python解释器程序来解释本程序的执行
         类似一种用法还有: #! /usr/bin/python
       下面这种说明要系统到/usr/bing/python这个路径下去找python解释器来解释本程序
        推荐：使用上一种，因为下面一种如果python安装路径不同就找不到python解释器
 2. #coding:UTF-8
        指示本源码的编码格式, python解释器默认使用ASCII编码  ，python解释器将按照这里指示的编码
        格式来解释下面的源码。
       注意： 编码的说明要么放在源文件的第一行，要么放在第二行
                      编码的说明格式只要符合这个表达式即可"coding[:=]\s*([-\w.]+)"
          #! /usr/bin/python
          # -*- coding: <encoding name> -*-
          
          #! /usr/bin/python
          # coding=<encoding name>
          
          #! /usr/bin/python
          # vim: set fileencoding=<encoding name> :
 3. __name__ : python模块内置的一个变量(可以使用dir()函数来获取所有内置变量)
                                          这里要注意一下__file__这个属性，写代码时用到得较多, 表示当前文件的全路径
 4. if __name__ == '__main__':
            当本模块被引入时，__name__的值将会是module的名字。 
            当本模块被独立执行时，__name__的值将会是"__main__"           
'''