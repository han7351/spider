#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time
import random
from  bs4 import BeautifulSoup


def a(url, pn):
  date = {'first': 'true', 'pn': str(pn), 'kd': '前端'}
  try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_Python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
        'Connection': 'keep-alive', 'Host': 'www.lagou.com'}
    a1 = requests.post(url, headers=headers, data=date)
    a2 = json.loads(a1.text)

    for i in range(15):
        positionId = a2['content']['positionResult']['result'][i]['positionId']
        companyShortName = a2['content']['positionResult']['result'][i]['companyShortName']
        workYear = a2['content']['positionResult']['result'][i]['workYear']
        district = a2['content']['positionResult']['result'][i]['district']
        positionName = a2['content']['positionResult']['result'][i]['positionName']
        formatCreateTime = a2['content']['positionResult']['result'][i]['formatCreateTime']
        salary = a2['content']['positionResult']['result'][i]['salary']
        print(str(i + 1) + '---' + str(positionId) + '----' + str(companyShortName) + '---' + str(
           positionName) + '----' + str(salary)+ '----' + str(workYear) + '----' + str(district) + '----' + str(formatCreateTime))
        print(str(positionId))

        headera = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
         'Referer': 'https://www.lagou.com/jobs/' + str(positionId) + '.html',
         'Connection': 'keep-alive', 'Host': 'www.lagou.com'}
        a3 = requests.get('https://www.lagou.com/jobs/' + str(positionId) + '.html', headers=headera)
        a3.encoding = 'utf-8'
        a4 = BeautifulSoup(a3.text, 'lxml')

        a5 = a4.find('dd', class_='job_bt')
        try:
         a6 = a5.get_text('\n', 'br/')

         print(a6)
         a7 = a4.find_all('input', type='hidden')
         print(a7[3]['value'])
        except:
            print(str(positionId))
        print('--------------------------------------------------------------------------------------------')
        time.sleep(random.randint(10, 17))
  except:
      print('未获取到原始网页')

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC'
for pn in range(1, 31):
    print('开始打印' + str(pn) + '页:')
    time.sleep(2)
    a(url, pn)
    print('-----------------------------------------\n')
    #time.sleep(random.randint(10, 15))
