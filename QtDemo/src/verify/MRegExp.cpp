/**************************************************************************
 * Copyright (c) 2012-2015
 * File: MRegExp.cpp
 * Version: 1.0
 * Description : 验证一些正则表达式的效果
 *
 * Modification History
 * -----------------------------------------------
 * Author: Xiao Deng 2012-09-14 创建新文件
 * -----------------------------------------------
 **************************************************************************/

#include "inc\verify\MRegExp.h"

/**
 * 构造函数
 */
MRegExp::MRegExp()
{

}

/**
 * 析构函数
 */
MRegExp::~MRegExp()
{

}

/**
 * 测试特定正则的效果
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
