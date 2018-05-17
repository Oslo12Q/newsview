# -*- coding: utf-8 -*-
import json
import time
import datetime
from django.http import HttpResponse
from django.db import connection
from django.db.models import Count

from django.shortcuts import render
from django.http import HttpResponse
from infoview.models import NewsInfo

def lanview(request):
    newsinfo = NewsInfo.objects.all()
    return render(request, 'lanview.html', {'newsinfo':newsinfo})
def timeview(request):
    return render(request, 'timeview.html')
def mapview(request):
    return render(request, 'mapview.html')
def topicview(request):
    return render(request, 'topicview.html')



'''
    # json时间处理
'''
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')   
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:    
            return json.JSONEncoder.default(self, obj) 

'''
    # 通用函数,返回json数据
''' 
def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp,cls=DateEncoder), content_type='application/json')


'''
    # 获取数据源
    # 函数（time_data）
    # 原生sql 去除时间格式错误的信息（0000-00-00）
'''
def time_data(request):
    arr_list = []
    try:
        now = datetime.datetime.now()
        dates = now.strftime('%Y-%m-%d')
        cursor = connection.cursor()
        sql = "SELECT * FROM infoview_newsinfo WHERE WZXX_FBSJ LIKE '%-%-%' AND WZXX_FBSJ != '0000-00-00' GROUP BY WZXX_FBSJ"
        rows = cursor.execute(sql)
        arr_objects = cursor.fetchall()
        for arr in arr_objects:
            wzxx = arr[2]
            news_Info= NewsInfo.objects.filter(WZXX_FBSJ = wzxx).count() # 每个时间段数量
            arr_data = [wzxx,news_Info,news_Info] # 数组格式
            arr_list.append(arr_data)
            
        return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = '',successResult=arr_list))

    except Exception, err:
        return get_json_response(request, dict(suc_id=0, ret_cd=500, ret_ts=long(time.time()),errorMsg = 'Server internal error',successResult=''))