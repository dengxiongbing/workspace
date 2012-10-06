/**************************************************************************
 * Copyright (c) 2012-2015
 * File: MRegExp.cpp
 * Version: 1.0
 * Description : ��֤һЩ������ʽ��Ч��
 *
 * Modification History
 * -----------------------------------------------
 * Author: Xiao Deng 2012-09-14 �������ļ�
 * -----------------------------------------------
 **************************************************************************/

#include "inc\verify\MRegExp.h"

/**
 * ���캯��
 */
MRegExp::MRegExp()
{

}

/**
 * ��������
 */
MRegExp::~MRegExp()
{

}

/**
 * �����ض������Ч��
 */  
MRegExp::checkEffect()
{
    QRegExp oRegExp(".*<script>(.*)</script>.*");
    oRegExp.setMinimal(true);

    QFile oFile("../dat/demo_2.3.html");
    if (!oFile.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        cout << "Open file failed!" << endl;
        return;
    }

    QString sHtml = "";
    QTextStream oTextStream(&oFile);    
    oTextStream >> sHtml;
    oFile.close();

    int nCnt = sHtml.count(oRegExp);
    cout << "Count is:" << nCnt << endl;

    int nPos = sHtml.indexOf(oRegExp);
    cout << "Pos is:" << nPos << endl;
}
