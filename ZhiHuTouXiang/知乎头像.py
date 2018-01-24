#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
import random

headers = {
    'accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/people/chen-dan-yi/following',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'x-udid': 'ABBCtzwlmAyPTrujtHeBXt6Snxbe64n6mJ8='
    }
a3 = requests.get('https://www.zhihu.com/people/zhe-ye-43-74-88/following', headers=headers)
#print (a3.text)
a4 = BeautifulSoup(a3.text,'html.parser')
a5 =  a4.find('button',class_ = 'Button PaginationButton PaginationButton-next Button--plain').previous_element.previous_element
print(a5)
for a6 in range(int(a5)):
 data = {
    'include': 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics',
    'offset':a6*20,
    'limit': 20}
 print(a6*20)
 a7 = requests.get('https://www.zhihu.com/api/v4/members/zhe-ye-43-74-88/followees?', headers=headers,data = data)

 a8 = json.loads(a7.text)
#print(a4)
 for a9 in a8['data']:
    a10 = a9['avatar_url_template']
    #print(a6.replace('{size}.jpg','xll.jpg'))
    a11 = requests.get(a10.replace('{size}.jpg','xll.jpg'))
    print(a9['name'])
    with open('C:\\Users\\p\\Desktop\\新\\'+a9['name']+'.jpg','wb') as  f:
      f.write(a11.content)
      f.close()
      time.sleep(random.randint(4,8))
     #time.sleep(5)
