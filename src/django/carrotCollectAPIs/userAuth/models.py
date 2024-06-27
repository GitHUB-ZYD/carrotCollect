from django.db import models
from django.utils import timezone
# Create your models here.

# 用户信息
class UserInfo(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True) 
    userName=models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    class Meta:
        db_table='UserInfo'
        
# 处理验证码
class VerifyCodeDB(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True) 
    email = models.CharField(max_length=40)
    code = models.CharField(max_length=10)
    # 这里必须是 函数对象 而不是函数的返回值
    dateTime = models.DateTimeField(default=timezone.now)
    expire = models.IntegerField()
    
    