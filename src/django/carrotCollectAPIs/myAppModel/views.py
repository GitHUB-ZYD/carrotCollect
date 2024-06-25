import json
from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

from django.http import HttpResponse

# 返回页面
def myAppModelIndex(request):
    return HttpResponse("这里是myAppModelIndex")

# 返回json数据
def returnJsonData(request):
    # 方法1
    # return HttpResponse(json.dumps({"姓名":"张逸东","称号":"王者66大神"}))
    # 方法2
    return JsonResponse({"姓名":"张逸东","称号":"王者66大神","请求":str(request)})
