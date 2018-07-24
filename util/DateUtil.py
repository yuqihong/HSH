# coding=utf-8
import datetime
import time
from _datetime import timedelta
def getDate(date_type):
    data = ""
    now = datetime.datetime.now()#今天
    if date_type == 'today':#当前时间
        data = now
    elif date_type == 'yesterday':#昨天
        data = now - timedelta(days=1)
    elif date_type == 'next_week_start':#下周第一天
        data = now - timedelta(days=now.weekday()-7)
    elif date_type == 'next_week_end':##下周最后一天
        data = now + timedelta(days=13-now.weekday())
    elif date_type == 'this_week_start':#本周第一天
        data = now - timedelta(days=now.weekday())
    elif date_type == 'this_week_end':##本周最后一天
        data = now + timedelta(days=6-now.weekday())  
    elif date_type == 'last_week_start':#上周第一天
        data = now - timedelta(days=now.weekday()+7) 
    elif date_type == 'last_week_end':#上周最后一天
        data = now - timedelta(days=now.weekday()+1)
    elif date_type == 'this_month_start':#本月第一天
        data = datetime.datetime(now.year, now.month, 1)
    elif date_type == 'this_month_end':#本月最后一天
        data = datetime.datetime(now.year, now.month + 1, 1) - timedelta(days=1)
    elif date_type == 'last_month_start':#上月第一天
        this_month_start = datetime.datetime(now.year, now.month, 1)
        last_month_end = this_month_start - timedelta(days=1)
        data = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    elif date_type == 'last_month_end':#上月最后一天
        this_month_start = datetime.datetime(now.year, now.month, 1)
        data = this_month_start - timedelta(days=1) 
    elif date_type == 'this_quarter_start':#本季第一天
        month = (now.month - 1) - (now.month - 1) % 3 + 1
        data = datetime.datetime(now.year, month, 1)
    elif date_type == 'this_quarter_end':#本季最后一天
        month = (now.month - 1) - (now.month - 1) % 3 + 1
        data = datetime.datetime(now.year, month + 3, 1) - timedelta(days=1)
    elif date_type == 'last_quarter_start':#上季第一天
        month = (now.month - 1) - (now.month - 1) % 3 + 1
        this_quarter_start = datetime.datetime(now.year, month, 1)
        last_quarter_end = this_quarter_start - timedelta(days=1)
        data = datetime.datetime(last_quarter_end.year, last_quarter_end.month - 2, 1)
    elif date_type == 'last_quarter_end':#上季最后一天
        month = (now.month - 1) - (now.month - 1) % 3 + 1
        this_quarter_start = datetime.datetime(now.year, month, 1)
        data = this_quarter_start - timedelta(days=1)
    elif date_type == 'this_year_start':#本年第一天
        data = datetime.datetime(now.year, 1, 1)
    elif date_type == 'this_year_end':#本年最后一天
        data = datetime.datetime(now.year + 1, 1, 1) - timedelta(days=1)
    elif date_type == 'last_year_start':#上年第一天
        this_year_start = datetime.datetime(now.year, 1, 1)
        last_year_end = this_year_start - timedelta(days=1)
        data = datetime.datetime(last_year_end.year, 1, 1)
    elif date_type == 'last_year_end':#上年最后一天
        this_year_start = datetime.datetime(now.year, 1, 1)
        data = this_year_start - timedelta(days=1)
    return str(data)[0:19]

#生成时间戳
def time_stamp():
    ct = time.time()
    time_stamp = time.strftime('%Y%m%d%H%M%S',time.localtime(ct))
    return time_stamp