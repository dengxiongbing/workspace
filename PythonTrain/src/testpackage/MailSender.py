#!/usr/bin/env python
#coding:UTF-8
#=================================================================
# @ Author : xiaodeng, Tencent, ISD, ITD, AutoTest_Tool
# @ Desc : 邮件发送封装
# @ FileName : MailSender.py 
# @ Date : 2011-10-13
# @ Remark :
#==================================================================
import smtplib;
from email.MIMEText import MIMEText;
from email.MIMEMultipart import MIMEMultipart;


SEP = ";";
LOG_DEBUG = 1;
LOG_ERROR = -1;

class MailSender(object):
    '''
         对邮件发送的封装，直接调用的Python标准库的邮件发送函数
    '''
    
    
    def __init__(self, logObj = None):
        '''
           日志对象进行初始化
        '''
        if(logObj != None):
            self.__logobj = logObj;
    
    
    def __log(self, logInfo, level):
        if(None == self.__logobj):
            print(logInfo);
        elif(LOG_DEBUG == level):
            self.__logobj.debug(logInfo);
        elif(LOG_ERROR == level):
            self.__logobj.error(logInfo);
        else:
            # 对于未知的日志种类作为错误对待
            raise Exception("unknown log level, " + logInfo);    
      
        
    def rstripstr (self, content, substr):
        if(substr == None) or (content == None):
            return content;
        temp = content;
        if(temp.endswith(substr)):
            lengthStr = len(substr);
            lengthContent = len(temp);
            temp = temp[0:lengthContent-lengthStr];
        return temp;
     
     
    def __genFullMailAddr(self, name, domain):
        '''
        name   : 单个的邮件地址，字符串格式
        domain : 邮件发送中要使用的域名地址
        return : name + @ + domain格式
        example: name = xiaodeng; domain = "tencent.com", return: xiaodeng@tencent.com
        '''
        if(None == name) or (None == domain):
            return name;
        
        addrSuffix = "@" + domain;
        temp = self.rstripstr(name, addrSuffix);
        
        return temp + addrSuffix;
            
            
    def __getMailAddrList(self, addrs, domain):
        '''
        addrs : 地址字符串或者是列表，支持两种格式：字符串或者是列表
        domain：邮件地址的域名
        return: (bool, msg) 第一个值代表是否成功，后一个如果出错时返回错误信息
        '''
        if(None == addrs) or ("" == addrs.strip()):
            return (False, None);
        
        addrList = [];
        if isinstance(addrs, str) or isinstance(addrs, list):
            if isinstance(addrs, str):
                tempList = addrs.split(SEP);
        
            for temp in tempList:
                fullAddr = self.__genFullMailAddr(temp, domain);
                if(None != fullAddr):
                    addrList.append(fullAddr);
        else:
            return (False, None);
        
        return (True, addrList);
    
    
    def __getLocalIp(self, ethName):
        '''
            echName: 网卡名，比如'eth0', 'eth1'
            return : 本机IP
        '''
        import socket;
        import fcntl;
        import struct; 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        # 0x8915 SIOCGIFADDR
        return socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', ethName[:15]))[20:24]);
     
           
    def send(self, content, to, cc, subject, sender, server = "192.168.1.27", port = "25", domain = "tencent.com", type = "html", charset = "utf-8"):
        '''
        content：要发送的邮件的文本内容，字符串格式
        to     : 邮件要发送到的收件人列表，['xiaodeng', 'terisli', 'rockenmeng'] 类似这种格式，类型为列表
        cc     : 邮件要抄送到的人名列表，['xiaodeng', 'terisli', 'rockenmeng'] 类似这种格式，类型为列表
        subject: 邮件的主题，字符串格式
        sender : 邮件的发送人，字符串格式
        server : 邮件服务器的IP， 字符串格式
        port   : 邮件服务器Port， 字符串格式 一般为25
        domain : 邮件发送过程中要使用的域名
        type   : 邮件的类型，字符串格式
        charset：邮件的编码格式，字符串类型
          返回值：成功(True, None)，失败(False, msg), msg为错误信息
        '''
        try:
            (isSucc, addrList) = self.__getMailAddrList(to, domain);
            if not isSucc:
                raise Exception("getMailAddrList failed, domain is:" + domain, + "; to is:" + to);
            mailToStr = SEP.join(addrList);
            self.__log("mailTo:" + mailToStr, LOG_DEBUG);
            
            receivers = addrList;
            
            (isSucc, addrList) = self.__getMailAddrList(cc, domain);
            if not isSucc:
                raise Exception("getMailAddrList failed, domain is:" + domain, + "; cc is:" + cc);
            mailCCStr = SEP.join(addrList);
            self.__log("mailCC:" + mailCCStr, LOG_DEBUG);
            
            # 这里要注意将CC的对象也添加到收件人列表里去，否则CC的人不会收到邮件
            for temp in addrList:
                receivers.append(temp); 
            
            mailSenderStr = self.__genFullMailAddr(sender, domain);
            self.__log("mailFrom:" + mailSenderStr, LOG_DEBUG);
            
            doc = MIMEText(content, type, charset);
            doc['Subject'] = subject;
            doc['From'] = mailSenderStr;
            doc['To'] = mailToStr;
            doc['Cc'] = mailCCStr;
            self.__log("body type:" + type, LOG_DEBUG);
            self.__log("body charset:" + charset, LOG_DEBUG);
            
            localIP = self.__getLocalIp("eth1");
            self.__log("local ip:" + localIP, LOG_DEBUG);
            
            smtpObj = smtplib.SMTP(server, port, localIP);
            self.__log("smtp server:" + server, LOG_DEBUG);
            self.__log("smtp port:" + port, LOG_DEBUG);
            smtpObj.sendmail(mailSenderStr, receivers, doc.as_string());
            self.__log("real receivers:" + str(receivers), LOG_DEBUG);
            smtpObj.close();
            
        except Exception, e:
            return(False, str(e));        
        
        return (True, None);
    
    
    def sendAttachment(self, content, attachPath, to, cc, subject, sender, server = "192.168.1.27", port = "25", domain = "tencent.com", type = "html", charset = "gb2312"):
        '''
        content：要发送的邮件的文本内容，字符串格式
        attachPath: 附件路径
        to     : 邮件要发送到的收件人列表，['xiaodeng', 'terisli', 'rockenmeng'] 类似这种格式，类型为列表
        cc     : 邮件要抄送到的人名列表，['xiaodeng', 'terisli', 'rockenmeng'] 类似这种格式，类型为列表
        subject: 邮件的主题，字符串格式
        sender : 邮件的发送人，字符串格式
        server : 邮件服务器的IP， 字符串格式
        port   : 邮件服务器Port， 字符串格式 一般为25
        domain : 邮件发送过程中要使用的域名
        type   : 邮件的类型，字符串格式
        charset：邮件的编码格式，字符串类型
          返回值：成功(True, None)，失败(False, msg), msg为错误信息
        '''
        try:
            (isSucc, addrList) = self.__getMailAddrList(to, domain);
            if not isSucc:
                raise Exception("getMailAddrList failed, domain is:" + domain, + "; to is:" + to);
            mailToStr = SEP.join(addrList);
            self.__log("mailTo:" + mailToStr, LOG_DEBUG);
            
            receivers = addrList;
            
            (isSucc, addrList) = self.__getMailAddrList(cc, domain);
            if not isSucc:
                raise Exception("getMailAddrList failed, domain is:" + domain, + "; cc is:" + cc);
            mailCCStr = SEP.join(addrList);
            self.__log("mailCC:" + mailCCStr, LOG_DEBUG);
            
            # 这里要注意将CC的对象也添加到收件人列表里去，否则CC的人不会收到邮件
            for temp in addrList:
                receivers.append(temp); 
            
            mailSenderStr = self.__genFullMailAddr(sender, domain);
            self.__log("mailFrom:" + mailSenderStr, LOG_DEBUG);
            
            doc = MIMEMultipart();
            doc['Subject'] = subject;
            doc['From'] = mailSenderStr;
            doc['To'] = mailToStr;
            doc['Cc'] = mailCCStr;
            self.__log("body type:" + type, LOG_DEBUG);
            self.__log("body charset:" + charset, LOG_DEBUG);
            
            mime = MIMEText(open(attachPath, 'rb').read(), 'base64', 'utf-8');
            self.__log("attachMent path:" + attachPath, LOG_DEBUG);
            mime["Content-Type"] = 'application/octet-stream';
            if(None == attachPath):
                fileName = "";
            else:
                import os;
                fileName = os.path.basename(attachPath);
            mime["Content-Disposition"] = "attachment; filename=" + fileName; 
            doc.attach(mime);
            
            body = MIMEText(content, type, charset);
            doc.attach(body);
            
            localIP = self.__getLocalIp("eth1");
            self.__log("local ip:" + localIP, LOG_DEBUG);
            
            smtpObj = smtplib.SMTP(server, port, localIP);
            self.__log("smtp server:" + server, LOG_DEBUG);
            self.__log("smtp port:" + port, LOG_DEBUG);
            smtpObj.sendmail(mailSenderStr, receivers, doc.as_string());
            self.__log("real receivers:" + str(receivers), LOG_DEBUG);
            smtpObj.close();
            
        except Exception, e:
            return(False, str(e));        
        
        return (True, None);

    
    __logobj = None;
  
    
    
if __name__ == '__main__':

    msg = "use program like this:  MailSender.py  mailPath  mailTo  mailCC  subject  mailsender  charset  attachmentPath\n" \
        + "NAME\n" \
        + " \tMailSender.py - send mail with python!\n" \
        + "SYNOPSIS\n" \
        + " \tMailSender.py  mailPath  mailTo  mailCC  subject  mailsender  charset  attachmentPath\n" \
        + "DESCRIPTION\n" \
        + " \tsend mail with python, encoding with 'gb2312' by default!\n" \
        + " \tmailPath, string type, the file path of your mail content!\n" \
        + " \tmailTo, string type, separated by ';'\n" \
        + " \tmailCC, string type, separated by ';'\n" \
        + " \tsubject, string type\n" \
        + " \tmailSender, string type\n" \
        + " \tcharset, string type, charset of mail body will be used!\n" \
        + " \tattachmentPath, string type, if there is no attachment, this parameter is not necessary!\n" \
        + "EXAMPLE\n" \
        + " \tMailSender.py /data/mail.html 'xiaodeng;howardren' 'erisenxu;terisli' test ISD_ATT\n" \
        + " \tMailSender.py /data/mail.html 'xiaodeng;howardren' '' test ISD_ATT\n" \
        + " \tMailSender.py /data/mail.html xiaodeng howardren test ISD_ATT utf-8\n" \
        + " \tMailSender.py /data/mail.html xiaodeng howardren test ISD_ATT gb2312 /data/attachment.tar\n" \
        + " \tMailSender.py /data/mail.html xiaodeng howardren test ISD_ATT utf-8 /data/attachment.tar\n";
        
    
    import sys;
    if(sys.argv == None) or (len(sys.argv) < 6):
        msg = "the system argv is null, this program need five arguments at least!\n" + msg;
        print (msg);
        sys.exit();
    
    try:
        mailPath = sys.argv[1];
        to = sys.argv[2];
        cc = sys.argv[3];
        subject = sys.argv[4];
        sender = sys.argv[5];
        
        if(len(sys.argv) >= 7):
            charset = sys.argv[6];
        else:
            charset = "gb2312";

        if(len(sys.argv) >= 8):
            attachPath = sys.argv[7];
        else:
            attachPath = None;
            
        mail = MailSender();
        
        content = None;
        if((None == mailPath) or ("" == mailPath)):
            raise Exception("mail path is null, please check your input!");
        else:
            file = open(mailPath, 'r');
            content = file.read();
            file.close();
            
        if(None == attachPath):
            (isSucc, msg) = mail.send(content, to, cc, subject, sender, "192.168.1.27", "25", "tencent.com", "html", charset);
            if(isSucc):
                print "send mail without attachment succ!";
            else:
                print "send mail without attachment failed! info:" + msg;
        else:
            (isSucc, msg) = mail.sendAttachment(content, attachPath, to, cc, subject, sender, "192.168.1.27", "25", "tencent.com", "html", charset);
            if(isSucc):
                print "send mail with attachment succ!";
            else:
                print "send mail  with attachment failed! info:" + msg;
    except Exception, e:
        print ("send mail failed! info is:" +  str(e));