# -*- coding: gbk -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from common import *
import var as v
import processreport as pr


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
    att2 = MIMEText(content,_subtype='html',_charset='gbk')
    msg.attach(att2)

    #attach3
    if pic_list is not None:
        cnt = 0
        for pic in pic_list:
            cnt += 1
            fp = open(pic, "rb")
            att3 = MIMEImage(fp.read())
            fp.close()
            att3.add_header('Content-ID', '<'+pic+'>')
            att3["Content-Type"] = 'application/octet-stream'
            att3["Content-Disposition"] = 'attachment; filename="chart.png"'
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


def generateMail(maillist, title, argsdic, attach=None,):
    content1 = """
        <p>�����Զ�����ִ������ %(sum)d ����pass %(pa)d ����ͨ���� %(percent)0.2f%%����ʱ %(time)0.2f Сʱ </p>
        <p>�����ն˹��������� %(onlinesum)d �Σ��ɹ����� %(onlinepa)d �Σ������� %(onlinepercent)0.2f%%��</p>
        """ % argsdic
        # {"sum": 120, "pa": 90, "percent": 20, "time": 36.66, "onlinesum": 3900, "onlinepa": 3000, "onlinepercent": 20}

    content2 = """
        <p>�����Զ�������wifi���²��ԣ���������ο���ͼ��</p>
        <p><img src="cid:throughput.png" alt="throughput.png" /></p>
        """
    content3 = """
        <p><img src="cid:total_memory_used.png" alt="total_memory_used.png" /></p>
        <p><span style="font-size:12px;">��Ϊϵͳ�Զ����ͣ�����ظ�������鿴������</span></p>
        """
    piclist = list()
    if os.path.isfile(v.MAIL_PIC1):
        piclist.append(v.MAIL_PIC1)
        contents = "{0}{1}".format(content1, content3)
        if os.path.isfile(v.MAIL_PIC2):
            piclist.append(v.MAIL_PIC2)
            contents = "{0}{1}{2}".format(content1, content2, content3)
        return sendMail(maillist, title, contents, attach, piclist)


if __name__ == '__main__':
    report = "R2D �ȶ���OTA 2.8.2.log"
    ret = pr.ProcessReport(report)
    ret.start()
    ret.join()

    if generateMail(["liujia5@xiaomi.com"], "test", ret.result, report):
        print "successful"
    else:
        print "failed"
