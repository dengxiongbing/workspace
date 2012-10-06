#!/usr/bin/env python
#coding:UTF-8
#tab:4 blank space
#=================================================================
# @ Author : xiaodeng, Tencent, ISD, ITD, AutoTest_Tool
# @ Desc : encapsulation of http operation
# @ FileName : http.py
# @ Date : 2012-06-09
# @ Remark :
#           Created on 2012-06-09
#==================================================================
import urllib2;

class Http:
    #测试
    def __init__(url):
        self._url = url;    
    
    def appendHeader(name, value):
        pass;

    def setContent(content):
        pass;        
    
    def getUrl():
        return self._url;
    
    def setUrl(url):
        self._url = url;

    def getReqObj():
        return self._request;

    def getRespObj():
        return self._response;
        
    _url = None;
    _request = None;
    _response = None;