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
        # zip类型附件
        att2 = MIMEApplication(open(attach2, 'rb').read())
        att2.add_header('Content-Disposition', 'attachment', filename="Test log.zip")
        msg.attach(att2)

    if attach3 is not None:
        # xlsx类型附件
        att3 = MIMEApplication(open(attach3, 'rb').read())
        att3.add_header('Content-Disposition', 'attachment', filename="Throughput.xlsx")
        msg.attach(att3)

    #attach5
    if pic_list is not None:
        cnt = 0
        for pic in pic_list:
            cnt += 1
            fp = open(pic, "rb")
            att5 = MIMEImage(fp.read(), _subtype="png")
            fp.close()
            att5.add_header('Content-ID', pic.split('\\')[-1])
            # att5["Content-Type"] = 'application/octet-stream'
            att5["Content-Type"] = 'image/png'
            msg.attach(att5)

    #attach4
    att4 = MIMEText(content, _subtype='html', _charset='utf8')
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


def generateMail(maillist, title, queue=None, attach1=None, attach2=None, attach3=None):
    if queue is not None:
        argsdic = queue.get(True)
        module = argsdic.get('module')
    else:
        raise Exception

    print argsdic
    content1 = """
        <p>无线终端：%s</p>
        """ % v.ANDROID_MODEL

    content2 = """
        <p>覆盖模块：%s</p>
        """ % "".join(module)

    content3 = """
        <p>本次自动化成功执行用例 %(ransum)d 个，通过%(ranpass)d 个，通过率 %(percent)0.2f%%。有%(error)d个脚本执行错误，
        共用时 %(time)0.2f 小时。无线终端尝试上线 %(onlinesum)d 次，成功上线 %(onlinepass)d 次，上线率 %(onlinepercent)0.2f%%</p>
        """ % argsdic

    content5 = """
        <img src="cid:%s" alt="%s" />
        """ % (v.MAIL_PIC2.split('\\')[-1], v.MAIL_PIC2.split('\\')[-1])

    content6 = """
        <img src="cid:%s" alt="%s" />
        """ % (v.MAIL_PIC5.split('\\')[-1], v.MAIL_PIC5.split('\\')[-1])

    content7 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC3.split('\\')[-1], v.MAIL_PIC3.split('\\')[-1])

    content8 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC6.split('\\')[-1], v.MAIL_PIC6.split('\\')[-1])

    content9 = """
        <p><img src="cid:%s" alt="%s" /></p>
        <p><img src="cid:%s" alt="%s" /></p>
        <p><span style="font-size:12px;">此为系统自动发送，请勿回复。</span></p>
        """ % (v.MAIL_PIC1.split('\\')[-1], v.MAIL_PIC1.split('\\')[-1], v.MAIL_PIC4.split('\\')[-1],
               v.MAIL_PIC4.split('\\')[-1])

    content10 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC7.split('\\')[-1], v.MAIL_PIC7.split('\\')[-1])

    content11 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC8.split('\\')[-1], v.MAIL_PIC8.split('\\')[-1])

    content12 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC9.split('\\')[-1], v.MAIL_PIC9.split('\\')[-1])

    content13 = """
        <img src="cid:%s" alt="%s" />
        """% (v.MAIL_PIC10.split('\\')[-1], v.MAIL_PIC10.split('\\')[-1])

    piclist = list()
    if argsdic.get("wandownload") is not None and argsdic.get("wanupload") is not None:
        content4 = """
            <p>路由器外网下载带宽 %(wandownload)s Mbps， 上传带宽 %(wanupload)s Mbps</p>
            """ % argsdic
        contents = content1 + content2 + content3 + content4
    else:
        contents = content1 + content2 + content3
    # 2.4g throughput chart
    if os.path.isfile(v.MAIL_PIC2):
        piclist.append(v.MAIL_PIC2)
        contents += content5
    if os.path.isfile(v.MAIL_PIC5):
        piclist.append(v.MAIL_PIC5)
        contents += content6
    if os.path.isfile(v.MAIL_PIC7):
        piclist.append(v.MAIL_PIC7)
        contents += content10
    if os.path.isfile(v.MAIL_PIC9):
        piclist.append(v.MAIL_PIC9)
        contents += content12

    # 5g throughput chart
    if os.path.isfile(v.MAIL_PIC3):
        piclist.append(v.MAIL_PIC3)
        contents += content7
    if os.path.isfile(v.MAIL_PIC6):
        piclist.append(v.MAIL_PIC6)
        contents += content8
    if os.path.isfile(v.MAIL_PIC8):
        piclist.append(v.MAIL_PIC8)
        contents += content11
    if os.path.isfile(v.MAIL_PIC10):
        piclist.append(v.MAIL_PIC10)
        contents += content13

    # cpu and memory chart
    if os.path.isfile(v.MAIL_PIC1) and os.path.isfile(v.MAIL_PIC4):
        piclist.append(v.MAIL_PIC1)
        piclist.append(v.MAIL_PIC4)
        contents += content9

    return sendMail(maillist, title, contents, attach1, attach2, attach3, piclist)


if __name__ == '__main__':
    import multiprocessing as mp
    v.ANDROID_MODEL = "Mi4 LTE"
    report = "R1CM 稳定版 2.10.12.log".decode("utf8").encode("gbk")
    q = mp.Queue() # tranlate test result to generateMail
    ret = pr.ProcessReport(report, q)
    ret.start()
    ret.join()

    if generateMail(["liujia5@xiaomi.com"], "test", q, report, report + ".zip"):
        print "successful"
    else:
        print "failed"
