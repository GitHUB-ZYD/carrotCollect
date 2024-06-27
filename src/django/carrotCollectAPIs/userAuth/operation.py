from utils import generateVerifyCode
from utils.sendMail import sendMail
from .models import *
from django.utils import timezone
# 用户注册  需要先发送验证码
def userRegister(userName,email,password,validCode):
    # filter返回一个列表，[]判断为false
    if UserInfo.objects.filter(email=email):
        return {'status':1,'msg':'该邮箱被注册过'}
    else:
        ifValid = ifCodeValid(email,validCode)
        if ifValid['status']==0:
            user = UserInfo.objects.create(userName=userName,password=password,email=email)
            return {'status':0,'msg':'注册成功','userInfo':user}
        else:
            return {'status':1,'msg':ifValid['msg']}

def userLogin(email,password):
    try:
        # get如果查不到，就抛出异常
        UserInfo.objects.get(email=email,password=password)
    except UserInfo.DoesNotExist as e:
        return {'status':1,'msg':'登陆失败'}
    return {'status':0,'msg':'登陆成功'}



# 给用户发送用于验证码
def sendVerificationCode2User(email,mode='password'):
    if mode=='password':
        try:
            UserInfo.objects.get(email=email)
        except UserInfo.DoesNotExist as e:
            return {'status':1,'msg':'邮箱不在数据库中'}
        code = generateVerifyCode.code(6)
        # 过期时间是 600秒
        codeObj = VerifyCodeDB.objects.create(email=email,code=code,expire=600)
        mailContent = f"""
你的找回密码的验证码是 {codeObj.code}
10分钟后失效
        """
        sendMailResult = sendMail(email,mailContent)
        if sendMailResult['status']==0:
            return {'status':0,'msg':codeObj.code}
        else:
            return {'status':1,'msg':"发送邮件失败"}
    if mode=='register':
        code = generateVerifyCode.code(6)
        codeObj = VerifyCodeDB.objects.create(email=email,code=code,expire=600)
        mailContent = f"""
你的注册验证码是 {codeObj.code}
10分钟后失效
        """
        sendMailResult = sendMail(email,mailContent)
        if sendMailResult['status']==0:
            return {'status':0,'msg':codeObj.code}
        else:
            return {'status':1,'msg':"发送邮件失败"}

def ifCodeValid(email,code):
    try:
        # get方法直接返回 obj对象，通过obj.key 就可以拿到元素的值
        codeObj =  VerifyCodeDB.objects.get(email=email,code=code)
        currentTime = timezone.now()
        if (currentTime-codeObj.dateTime).total_seconds() > codeObj.expire:
            return {'status':1,'msg':'验证码过期'}
        return {'status':0,'msg':'验证码有效'}
    except VerifyCodeDB.DoesNotExist as e:
        return {'status':1,'msg':'验证码错误'}
    
# 找回密码
def sendPwd2User(email,code):
    ifValid = ifCodeValid(email,code)
    if ifValid['status']==0:
        user = UserInfo.objects.get(email=email)
        mailContent = f"""
你的密码是 {user.password}
        """
        sendMail(user.email,mailContent=mailContent)
    else:
        return {'status':1,"msg":ifValid['msg']}


if __name__=='__main__':
    import userAuth.operation as op
    op.userRegister("zyd","123123","mail")
    op.userLogin("mail","123123")