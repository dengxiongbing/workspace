/**************************************************************************
 * Copyright (c) 2012-2015
 * File: Main.h
 * Version: 1.0
 * Description : �������
 *
 * Modification History
 * -----------------------------------------------
 * Author: Xiao Deng 2012-09-14 �������ļ�
 * -----------------------------------------------
 **************************************************************************/

#include "MQtDemo.h"
#include "verify/MRegExp.h"

int main(int argc, char *argv[])
{
    QApplication oApp(argc, argv);

    MRegExp oRegExp;
    oRegExp.checkEffect();
    
    return 0;
}
