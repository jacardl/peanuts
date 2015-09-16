# -*- coding: gbk -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from common import *
import var as v


def sendMail(to_list, sub, content, attach=None, pic_list=None):  #to_list���ռ��ˣ�sub�����⣻content���ʼ�����

    me="<"+v.MAIL_USER+"@"+v.MAIL_POSTFIX+">"   #�յ��ź󣬽�����������ʾ
    msg = MIMEMultipart()   #����һ��ʵ��
    msg['Subject'] = sub    #��������
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    # attach1
    if attach is not None:
        att1 = MIMEText(open(attach, 'rb').read(), "base64", "gb2312")
        att1["Content-Type"] = "application/octet-stream"
        att1["Content-Disposition"] = 'attachment;filename=Test report.txt'
        msg.attach(att1)

    #attach2
    att2 = MIMEText(content,_subtype='html',_charset='gb2312')
    msg.attach(att2)

    #attach3
    if pic_list is not None:
        cnt = 0 ;
        for pic in pic_list :
            cnt = cnt + 1 ;
            fp = open(pic,"rb");
            att3 = MIMEImage(fp.read())
            fp.close()
            att3.add_header('Content-ID', '<'+pic+'>')
            att3["Content-Type"] = 'application/octet-stream'
            att3["Content-Disposition"] = 'attachment; filename="Total memory used.png"'
            msg.attach(att3)


    try:
        s = smtplib.SMTP()
        s.connect(v.MAIL_HOST)  #����smtp������
        # s.login(mail_user,mail_pass)  #��½������
        s.sendmail(me, to_list, msg.as_string())  #�����ʼ�
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    cli = SshCommand(2)
    cli.connect("192.168.31.1", "", "")
    content ="""<html><body><img src="cid:Total_memory_used.png" alt="Total_memory_used.png"></body></html><small>��Ϊϵͳ�Զ����ͣ�����ظ�������鿴������</small>"""

    if sendMail(["liujia5@xiaomi.com"], cli.setMailTitle(), content, "temp.xls", ["Total_memory_used.png"]):
        print "successful"
    else:
        print "failed"
