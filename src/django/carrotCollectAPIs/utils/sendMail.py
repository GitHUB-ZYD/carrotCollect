import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
def sendMail(toEmail,mailContent):
    try:
        # 1. 连接邮箱服务器
        con = smtplib.SMTP_SSL('smtp.qq.com', 465)
        # 2. 登录邮箱
        con.login('2720725749@qq.com', 'xqpvrwiyumwpdhbc')
        # con.login('2429079654@qq.com', 'mftyyjhdahihdife')
        # 2. 准备数据
        # 创建邮件对象
        msg = MIMEMultipart()
        # 设置邮件主题
        subject = Header("carrotCollect的验证码", 'utf-8').encode()
        msg['Subject'] = subject

        # 设置邮件发送者
        msg['From'] = '2720725749@qq.com'
        # msg['From'] = '2429079654@qq.com'
        # To 填写要接收的邮箱
        msg['To'] = toEmail
        # 添加文字内容
        text = MIMEText(mailContent, 'plain', 'utf-8')
        msg.attach(text)
        con.sendmail(msg['From'],  msg['To'], msg.as_string())
        con.quit()
    # except Exception as e:
    #     return "Sorry, the email failed to send due to possible network issues. Please try again."
    # return "Thank you for your feedback. We have received your email!"
    except Exception as e:
        return {'status':1,'msg':'发送邮件失败，请检查邮箱是否有效'}
    return {'status':0,'msg':'成功'}