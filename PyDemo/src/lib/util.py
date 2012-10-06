#!/usr/bin/env python
#coding:UTF-8
#tab key:has replaced with 4 blank space
#=================================================================
# @ Author : xiaodeng, Tencent, ISD, ITD, AutoTest_Tool
# @ Desc : utils method
# @ FileName : util.py
# @ Date : 2012-06-09
# @ Remark :
#           Created on 2012-06-09
#==================================================================
import os;
import sys;
PARAM_ERR = "param error"
EMPTY_STR = "";

EXEC_CMD_ERR = -1;
EXEC_CMD_SUCC = 0;
def execWithoutPara(cmd, isPrintSysOut = False):
    '''执行不带参数的第三方命令的执行器 '''
    output = EMPTY_STR;
    retCode = EXEC_CMD_ERR;
    isSucc = False;
    if (type(EMPTY_STR) != type(cmd)) and (type(False) != type(isPrintSysOut)):
        output = PARAM_ERR
        return (isSucc, retCode, output);      
    import subprocess;
    # 采用独立shell进程，管道模式，标准错误重定向到标准输出
    proc = subprocess.Popen(cmd, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT);    
    retCode = proc.poll();
    try:
        while (None == retCode):
            proc.stdout.flush();   
            buf = proc.stdout.readline();
            if(isPrintSysOut): sys.stdout.write(buf);            
            output = output + buf;            
            retCode = proc.poll();
        proc.stdout.flush();
        buf = proc.stdout.read();        
        if(isPrintSysOut): sys.stdout.write(buf);
        output = output + buf;
        isSucc = True;
    except IOError, e:            
        if isPrintSysOut: sys.stdout.write("there is io error: " + str(e));
        output = output + "\n" + str(e);  
    except Exception, e:
        if isPrintSysOut: sys.stdout.write("there is exception: " + str(e));
        output = output + "\n" + str(e);

    output = str(output).strip(" \t\n");
    return (isSucc, retCode, output);

def execWithPara(cmd, para, isPrintSysOut = False):
    '''执行带参数的第三方命令的执行器 '''
    output = EMPTY_STR;
    retCode = EXEC_CMD_ERR;
	isSucc = False;
    if (type(EMPTY_STR) != type(cmd)) and (EMPTY_STR == cmd.strip()):
        output = PARAM_ERR
        return (isSucc, retCode, output);
    if (not para): return execWithoutPara(cmd, isPrintSysOut);
    if (type(EMPTY_STR) != type(para)):
        output = PARAM_ERR
        return (isSucc, retCode, output);
    try:
        import subprocess;
        # 采用独立shell进程，管道模式，标准错误重定向到标准输出
        proc = subprocess.Popen(cmd, shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT);
        # 对于需要交互的程序不能实时获取到输出数据
        (out, err) = proc.communicate(para);
        retCode = proc.wait();
        output = out;
		isSucc = True;
	except IOError, e:            
        if isPrintSysOut: sys.stdout.write("there is io error: " + str(e));
        output = output + "\n" + str(e);
    except Exception, e:
		if isPrintSysOut: sys.stdout.write("there is exception: " + str(e));
		output = output + "\n" + str(e);        
        
    return (isSucc, retCode, output);    


##############http method##############
HTTP_ERR_RETCODE = -1
def openUrl(url, timeout = 20):    
    '''A simple way to open url
       url:     the URI to be opened, it must start with 'http://'
       timeout: time out of connecting to server
       return:  the tuple of status code and error message, HTTP_ERR_RETCODE means failed!
    '''
    errMsg = EMPTY_STR;
    if None == url:
        errMsg = PARAM_ERR
        return (HTTP_ERR_RETCODE, errMsg);
    if (type(EMPTY_STR) == type(url)) and (EMPTY_STR == url.strip()):
        errMsg = PARAM_ERR
        return (HTTP_ERR_RETCODE, errMsg);
    
	tempUrl = url;
    from urllib2 import HTTPError, socket, urlopen;
    try:        
        socket.setdefaulttimeout(timeout)
        tempUrl = urlEncode(tempUrl);
        response = urlopen(tempUrl);        
        if not response:
            errMsg = "response is none";
            return (HTTP_ERR_RETCODE, errMsg);        
        try:
            response.close();
        except Exception, closeE:
            errMsg = "close response failed," + str(closeE);
        retCode = 200;
    except HTTPError, e:
        errMsg = str(e);        
        retCode = e.code;
    except Exception, e:
        errMsg = str(e);
        retCode = HTTP_ERR_RETCODE;
        
    return (retCode, errMsg);

def urlEncode(value):
    from urllib import urlencode;
    return urlencode(value);


##############string method##############
def lstripstr(content, substr):
'''strip a substring from the header of string'''
    if(None == substr) or (None == content):
        return content;
    if(type(EMPTY_STR) != type(content)):
        return content;   
    temp = content;
    lengthStr = len(substr);
    while(temp.startswith(substr)):        
        lengthContent = len(temp);        
        temp = temp[lengthStr:lengthContent];        
    return temp;

def rstripstr(content, substr):
'''strip a substring from the end of string'''
    if(None == substr) or (None == content):
        return content;
    if(type(EMPTY_STR) != type(content)):
        return content;
    temp = content;
    lengthStr = len(substr);
    while(temp.endswith(substr)):        
        lengthContent = len(temp);
        temp = temp[0:lengthContent - lengthStr];
    return temp;

def stripstr(content, substr):
'''strip a substring from the header and end of string'''
    if(None == substr) or (None == content):
        return content;
    if(type(EMPTY_STR) != type(content)):
        return content;
    temp = content;
    lengthStr = len(substr);
    while(temp.startswith(substr)):
        lengthContent = len(temp);
        temp = temp[lengthStr:lengthContent];
    while(temp.endswith(substr)):
        lengthContent = len(temp);
        temp = temp[0:lengthContent - lengthStr];
    return temp;

def contain(srcStr, destStr):
    errMsg = EMPTY_STR;
    if(type(EMPTY_STR) != type(srcStr)):
        errMsg = PARAM_ERR
        return (False, errMsg);
    index = srcStr.find(str(destStr));
    if(index < 0):
        errMsg = "dest string didn't include in source string";
        return (False, errMsg);
    else:
        return (True, errMsg);

		
##############system method##############
def getLocalIP(ethName='eth1'):
    errMsg = EMPTY_STR;
	try:
        import platform;
        sysName = platform.system();
        import socket;
        if ('Windows' == sysName):	
            return (socket.gethostbyname(socket.gethostname()), errMsg);
        elif ('Linux' == sysName):
            import fcntl;
            import struct;
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
            ip = socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', ethName[:15]))[20:24]);
            return (ip, errMsg)
        else:
            errMsg = "unsupport os system";
            return (None, errMsg);
    except Exception, e:
        errMsg = "exeption: " + str(e); 
        return (None, errMsg); 

def getCurUser():
    cmdStr = "whoami";
    (isSucc, retCode, output) = execWithoutPara(cmdStr);
    if (not isSucc) or (EXEC_CMD_SUCC != retCode): return EMPTY_STR;
    return output;
    
SysBit64 = "64bit"
SysBit32 = "32bit";
def getSysBit():
    import platform;
    (systemBit, info) = platform.architecture();
    if(systemBit) and (EMPTY_STR != systemBit):
        systemBit = systemBit.lower();
        if(SysBit32 == systemBit) or (SysBit64 == systemBit):
            return systemBit;
    return EMPTY_STR;
    
def getName():
    '''
    返回计算机在网络上的名字
    '''
    import platform;
    return platform.node();

def getCpuCount():
    errMsg = EMPTY_STR;
    try:    
        fileObj = open('/proc/cpuinfo');
        content = fileObj.read();
    except Exception, e:
        errMsg = str(e)
        return (None, errMsg);
    cpuCount = content.count('processor\t:');
    if cpuCount <= 0:
        errMsg = "Get the count is " + str(cpuCount) + ", invalid!"
        cpuCount = None;
    
    return (cpuCount, errMsg);

def killProc(pid):
    errMsg = EMPTY_STR;
    if (type(1) != type(pid)) or (pid < 1):
        errMsg = PARAM_ERR;
        return (False, errMsg);
    try:
        os.kill(pid, signal.SIGTERM);
    except Exception, e:
        errMsg = str(e);
        return (False, errMsg);
    return (True, errMsg);

def getPidByName(procName):
    pids = [];
    cmdStr = "ps axu | grep " + str(name);    
    (isSucc, retCode, output) = execWithoutPara(cmdStr);    
    if isSucc and output and (EXEC_CMD_SUCC == retCode):
        pids = [];
        output = str(output).strip("\n");
        lines = output.split("\n");        
        for line in lines:
            tokens = line.split();
            if len(tokens) < 2: continue;            
            pid = int(tokens[1]);
            if pid: pids.append(pid);    
    
    return pids;

def getGccVer():
    cmdStr = "/usr/bin/gcc -v";    
    (isSucc, output, retCode) = execWithoutPara(cmdStr);
    
    gccVer = "-";    
    if (not isSucc) or (retCode != 0): return gccVer;     
    regExpStr = "gcc\s+version\s+(.*)";
    import re;
    regexExp = re.compile(regExpStr, re.I);
    matches = regexExp.findall(output);            
    if len(matches) > 0:            
        gccVer = matches[0].strip();
    
    return gccVer;

def encodePsw(psw):
    try:
        import base64;
        ''' 采用最简单的base64方法对字符串进行加密 '''
        return (True, base64.encodestring(psw));
    except Exception, e:
        errMsg = str(e);
        return (False, errMsg);

def decodePsw(encodePsw):
    try:
        ''' 对用base64方法加密的密文进行解密  '''
        return (True, base64.decodestring(encodePsw));        
    except Exception, e:
        errMsg = str(e);
        return (True, errMsg);

##############path method##############
def createPath(path, isDir = False):
    errMsg = EMPTY_STR;
    if (not path) or (type(EMPTY_STR) != type(path)):
        errMsg = PARAM_ERROR;
        return (False, errMsg);
    if(os.path.exists(path)):
        errMsg = "path has exist!";
        return (True, errMsg);        
    try:
        parentDir = os.path.dirname(path);
        if(not os.path.exists(parentDir)): os.makedirs(parentDir);
        if(isDir):
            os.mkdir(path);
        else:
            fileObj = open(path, "w");
            fileObj.close();
    except Exception, e:
        errMsg = str(e);
        return (False, errMsg);
    return (True, errMsg);

def copyPath(srcPath, destPath):
    # 这里要调整到能支持源或者目的都可以为目录或源
    errMsg = EMPTY_STR;
    try:
        import shutil;
        shutil.copy(srcPath, destPath);
        return (True, errMsg);
    except Exception, e:
        errMsg = str(e);
        return (False, errMsg);
      
def rmPath(path):
    errMsg = EMPTY_STR
    if(not os.path.exists(path)):return (True, errMsg);
    try:
        import shutil;
        if(os.path.isdir(path)):
            shutil.rmtree(path, True);
        else:
            os.remove(path);         
    except Exception, e:
        errMsg = str(e);
        return (False, errMsg);
    return (True, errMsg)

def rmBfTime(dir, days):
    if os.path.exists(dir):
        # 目前的这种处理方式只支持文件名是规则的按时间来命名的情况
        # 否则需要对sort进行传额外的参数，提供按文件进行比较的函数
        subDirs = os.listdir(dir);
        subDirs.sort();
        
        rmLen = 0;
        
        if len(subDirs) > days:
            rmLen = len(subDirs) - days;
        
        for i in range(0, rmLen):
            rmPath(os.path.join(dir, subDirs[i]));

CHECKMODE_ALL_BUT_LAST = 0;
CHECKMODE_ALL = 1;
CHECKMODE_NONE = 2; 
def getRealPath(path, checkMode=0):
    """ 获取文件的实际路径    
        path: 待获取实际路径的路径参数
        checkMode: 检查路径是否存在的模式，
            0代表检查路径除最底层的文件或目录外的所有部分是否存在
            1代表检查路径所有部分是否存在
            2代表不检查路径的所有部分是否存在
        如果顺利获取则返回实际的路径，否则出现任何错误都返回(None，错误信息）这样一个值对
        # readlink -f path 路径的最后一层允许不存在
        # readlink -e path 路径指定的文件必须存在
        # readlink -m path 路径指定的文件不检查是否存在
    """
    realPath = None;
    cmd = "readlink";
    if(path == None) or (path == ""):
        return (realPath, "path for function getRealPath is null!");
    elif(checkMode == CHECKMODE_ALL_BUT_LAST):
        cmd = cmd + " -f " + path;
    elif(checkMode == CHECKMODE_ALL):
        cmd = cmd + " -e " + path;
    elif(checkMode == CHECKMODE_NONE):
        cmd = cmd + " -m " + path;
    else:
        return (realPath, "checkMode for function getrealPath only can choose from 0(readlink -f),1(readlink -e),2(readlink -m),but you input " + str(checkMode));
    
    (isSucc, output, retCode) = execute(cmd);
    if isSucc and (retCode == SUCC_CODE) and (output.strip(" \n") != ""):
        realPath = output;
    else:
        return (realPath, output);
    
    return (realPath, "successfully!"); 


##############data method##############
def roundOff(data, keepBit = 2):
    """ 对浮点数进行四舍五入处理  """
    if(type(0.1) == type(data)):
        import decimal;
        return str(decimal.Decimal(str(round(data, keepBit))));
    else:
        return data;


##############Time method##############
def getLocalTime(seconds = None):
    ''' 获取本地时间 
        
        seconds: 整形值, 表示自Epoch以来全部时间的秒数 
        return : 表示seconds代表的时间的一个元组
    '''
    if(None == seconds):        
        seconds = time.time();
    # 注意这里如果不传参数的话localtime也会自动获取当前时间        
    localTime = time.localtime(seconds);
    
    return localTime;


def getCurTime(formatStr = "%H%M"):
    ''' 获取系统当前时间(小时分钟秒)
    
        formatStr : 字符串类型，用来指明输出时间的格式
        return    : 指定格式的当前时间
    '''
    localTime= getLocalTime();    
    
    return time.strftime(formatStr, localTime);
    
     
def getCurDate(formatStr = "%y-%m-%d"):
    ''' 获取系统当前时间(年月日)
    
        formatStr : 字符串类型，用来指明输出日期的格式
        return    : 指定格式的当前日期
    '''
    localTime= getLocalTime();
    
    return time.strftime(formatStr, localTime);
	
HTTP_ERR_RETCODE = -1
EMPTY_STR = ""
PARAM_ERR = "param error!"
def openUrl(url, timeout = 20):    
    '''A simple way to open url
       url:     the URI to be opened, it must start with 'http://'
       timeout: time out of connecting to server
       return:  the status code, HTTP_ERR_RETCODE if failed!
    '''
    errMsg = EMPTY_STR;
    if None == url:
        errMsg = PARAM_ERR
        return (HTTP_ERR_RETCODE, errMsg);
    if (type(EMPTY_STR) == type(url)) and (EMPTY_STR == url.strip()):
        errMsg = PARAM_ERR
        return (HTTP_ERR_RETCODE, errMsg);
    from urllib2 import HTTPError, socket, urlopen;
    try:        
        socket.setdefaulttimeout(timeout)
        response = urlopen(url);        
        if not response:
            errMsg = "response is none";
            return (HTTP_ERR_RETCODE, errMsg);        
        try:
            response.close();
        except Exception, closeE:
            errMsg = "close response failed," + str(closeE);
        retCode = 200;
    except HTTPError, e:
        errMsg = str(e);        
        retCode = e.code;
    except Exception, e:
        errMsg = str(e);
        retCode = HTTP_ERR_RETCODE;
        
    return (retCode, errMsg);
