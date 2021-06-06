# coding=utf-8
import requests
from datetime import datetime
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#from T2Api.t2Request import request


def job():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
# 每隔5分钟 运行一次 job 方法
    '''调试时使用secons=3，运行成功每3秒运行一次'''
    scheduler.add_job(job, 'interval', minutes=5)
    url = 'https://www.baidu.com'
    resp = requests.get(url, verify=False)
    print(resp.status_code)
    print(resp.text)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
