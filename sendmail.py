# -*- coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import var as v
from common import *
import processreport as pr


def sendMail(to_list, sub, content, attach1=None, attach2=None, pic_list=None):  #to_list：收件人；sub：主题；content：邮件内容

    me="<"+v.MAIL_USER+"@"+v.MAIL_POSTFIX+">"   #收到信后，将按照设置显示
    msg = MIMEMultipart()   #创建一个实例
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    # attach1
    if attach1 is not None:
        # text 类型附件
        att1 = MIMEText(open(attach1, 'rb').read(), "base64", "gb2312")
        att1["Content-Type"] = "application/octet-stream"
        att1["Content-Disposition"] = 'attachment;filename=Test Report.txt'
        msg.attach(att1)

    if attach2 is not None:
        # xlsx类型附件
        att2 = MIMEApplication(open(attach2, 'rb').read())
        att2.add_header('Content-Disposition', 'attachment', filename="Memory Tracking.xlsx")
        msg.attach(att2)

    #attach2
    att3 = MIMEText(content, _subtype='html', _charset='utf8')
    msg.attach(att3)

    #attach3
    if pic_list is not None:
        cnt = 0
        for pic in pic_list:
            cnt += 1
            fp = open(pic, "rb")
            att4 = MIMEImage(fp.read())
            fp.close()
            att4.add_header('Content-ID', '<'+pic+'>')
            att4["Content-Type"] = 'application/octet-stream'
            att4["Content-Disposition"] = 'attachment; filename="chart.png"'
            msg.attach(att4)

    try:
        s = smtplib.SMTP()
        s.connect(v.MAIL_HOST)  #连接smtp服务器
        # s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print "connect to mail server and send mail failed!"
        return False


def generateMail(maillist, title, queue=None, attach1=None, attach2=None):
    if queue is not None:
        argsdic = queue.get(True)
    else:
        raise Exception
    content1 = """
        <p>本次自动化共执行用例 %(sum)d 个，pass %(pa)d 个，通过率 %(percent)0.2f%%，用时 %(time)0.2f 小时 </p>
        <p>无线终端共尝试上线 %(onlinesum)d 次，成功上线 %(onlinepa)d 次，上线率 %(onlinepercent)0.2f%%。</p>
        """ % argsdic
        # {"sum": 120, "pa": 90, "percent": 20, "time": 36.66, "onlinesum": 3900, "onlinepa": 3000, "onlinepercent": 20}

    content2 = """
        <p>本次自动化覆盖wifi吞吐测试，具体结果请参看下图：</p>
        <p><img src="cid:throughput.png" alt="throughput.png" /></p>
        <p><img src="cid:throughput_in_AES.png" alt="throughput_in_AES.png" /></p>
        <p><img src="cid:throughput_in_Clear.png" alt="throughput_in_Clear.png" /></p>
        <p><img src="cid:throughput_in_TKIP.png" alt="throughput_in_TKIP.png" /></p>
        """
    content3 = """
        <p><img src="cid:total_memory_used.png" alt="total_memory_used.png" /></p>
        <p><span style="font-size:12px;">此为系统自动发送，请勿回复，测试报告及内存跟踪详情查看附件。</span></p>
        """
    piclist = list()
    if os.path.isfile(v.MAIL_PIC1):
        piclist.append(v.MAIL_PIC1)
        contents = "{0}{1}".format(content1, content3)
        if os.path.isfile(v.MAIL_PIC2):
            piclist.append(v.MAIL_PIC2)
            if os.path.isfile(v.MAIL_PIC3%"AES"):
                piclist.append(v.MAIL_PIC3%"AES")
            if os.path.isfile(v.MAIL_PIC3%"TKIP"):
                piclist.append(v.MAIL_PIC3%"TKIP")
            if os.path.isfile(v.MAIL_PIC3%"Clear"):
                piclist.append(v.MAIL_PIC3%"Clear")
            contents = "{0}{1}{2}".format(content1, content2, content3)
        return sendMail(maillist, title, contents, attach1, attach2, piclist)


if __name__ == '__main__':
    import multiprocessing as mp
    report = "R1D 开发版OTA 2.11.38.log".decode("utf8").encode("gbk")
    q = mp.Queue() # tranlate test result to generateMail
    ret = pr.ProcessReport(report, q)
    ret.start()
    ret.join()

    # if generateMail(["liujia5@xiaomi.com"], "test", ret.result, report):
    if generateMail(v.MAILTO_LIST, "【R1D 开发版OTA 2.11.38】自动化测试报告", q, report, v.MAIL_XLSX):
        print "successful"
    else:
        print "failed"
