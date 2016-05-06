# -*- coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import var as v
from common import *
import processreport as pr


def sendMail(to_list, sub, content, attach1=None, attach2=None, attach3=None, pic_list=None):  #to_list：收件人；sub：主题；content：邮件内容

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

    if attach3 is not None:
        # xlsx类型附件
        att3 = MIMEApplication(open(attach3, 'rb').read())
        att3.add_header('Content-Disposition', 'attachment', filename="Throughput.xlsx")
        msg.attach(att3)

    #attach4
    att4 = MIMEText(content, _subtype='html', _charset='utf8')
    msg.attach(att4)

    #attach5
    if pic_list is not None:
        cnt = 0
        for pic in pic_list:
            cnt += 1
            fp = open(pic, "rb")
            att5 = MIMEImage(fp.read(), _subtype="png")
            fp.close()
            att5.add_header('Content-ID', '<'+pic+'>')
            att5["Content-Type"] = 'application/octet-stream'
            att5["Content-Disposition"] = 'attachment; filename="chart.png"'
            msg.attach(att5)

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


def generateMail(maillist, title, queue=None, attach1=None, attach2=None, attach3=None):
    if queue is not None:
        argsdic = queue.get(True)
        module = argsdic.get('module')
    else:
        raise Exception

    print argsdic
    content5 = """
        <p>无线终端：%s</p>
        """ % v.ANDROID_MODEL

    content4 = """
        <p>覆盖模块：%s</p>
        """ % "".join(module)

    content1 = """
        <p>本次自动化成功执行用例 %(sum)d 个，通过%(ranpass)d 个，通过率 %(percent)0.2f%%。有%(error)d个脚本执行错误，共用时 %(time)0.2f 小时。无线终端尝试上线 %(onlinesum)d 次，成功上线 %(onlinepass)d 次，上线率 %(onlinepercent)0.2f%%</p>
        """ % argsdic

    content2 = """
        <p>WiFi吞吐测试概览如下，详细数据查看附件：</p>
        <p><img src="cid:throughput_2g.png" alt="throughput_2g.png" /></p>
        <p><img src="cid:throughput_5g.png" alt="throughput_5g.png" /></p>
        """
    content3 = """
        <p>系统状态如下，详细数据查看附件：</p>
        <p><img src="cid:total_memory_used.png" alt="total_memory_used.png" /></p>
        <p><img src="cid:current_cpu_load.png" alt="current_cpu_load.png" /></p>
        <p><span style="font-size:12px;">此为系统自动发送，请勿回复。</span></p>
        """
    piclist = list()
    if os.path.isfile(v.MAIL_PIC1) and os.path.isfile(v.MAIL_PIC4):
        piclist.append(v.MAIL_PIC1)
        piclist.append(v.MAIL_PIC4)
        contents = "{0}{1}{2}{3}".format(content5, content4, content1, content3)
        if os.path.isfile(v.MAIL_PIC2):
            piclist.append(v.MAIL_PIC2)
            if os.path.isfile(v.MAIL_PIC3):
                piclist.append(v.MAIL_PIC3)
            contents = "{0}{1}{2}{3}{4}".format(content5, content4, content1, content2, content3)
        return sendMail(maillist, title, contents, attach1, attach2, attach3, piclist)


if __name__ == '__main__':
    import multiprocessing as mp
    v.ANDROID_MODEL = "Mi4 LTE"
    report = "R2D 开发版OTA 2.13.16.log".decode("utf8").encode("gbk")
    q = mp.Queue() # tranlate test result to generateMail
    ret = pr.ProcessReport(report, q)
    ret.start()
    ret.join()

    if generateMail(["liujia5@xiaomi.com"], "test", q, report, v.MAIL_XLSX, v.TEST_SUITE_LOG_PATH + v.MAIL_THROUGHPUT_XLSX):
        print "successful"
    else:
        print "failed"
