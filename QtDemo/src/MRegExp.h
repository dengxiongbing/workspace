/**************************************************************************
 * Copyright (c) 2012-2015
 * File: MRegExp.h
 * Version: 1.0
 * Description : 验证一些正则表达式的效果
 *
 * Modification History
 * -----------------------------------------------
 * Author: Xiao Deng 2012-09-14 创建新文件
 * -----------------------------------------------
 **************************************************************************/

#ifndef M_REGEXP_H
#define M_REGEXP_H

#include "MQtDemo.h"

class MRegExp
{
public:
    /**
     * 构造函数
     */
    MRegExp();

    /**
     * 析构函数
     */
    ~MRegExp();

private:
    /**
     * 测试特定正则的效果
     */    
    void checkEffect();
};

#endif