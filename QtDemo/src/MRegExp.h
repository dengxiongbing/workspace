/**************************************************************************
 * Copyright (c) 2012-2015
 * File: MRegExp.h
 * Version: 1.0
 * Description : ��֤һЩ������ʽ��Ч��
 *
 * Modification History
 * -----------------------------------------------
 * Author: Xiao Deng 2012-09-14 �������ļ�
 * -----------------------------------------------
 **************************************************************************/

#ifndef M_REGEXP_H
#define M_REGEXP_H

#include "MQtDemo.h"

class MRegExp
{
public:
    /**
     * ���캯��
     */
    MRegExp();

    /**
     * ��������
     */
    ~MRegExp();

private:
    /**
     * �����ض������Ч��
     */    
    void checkEffect();
};

#endif