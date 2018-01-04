#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 19:56
# @Author  : Aries
# @Site    : 
# @File    : webshu.py
# @Software: PyCharm Community Edition
import requests
search_name = '手机'
#url = "https://s.taobao.com/search?q=" + str(
 #   search_name) + "&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=0"
url = 'https://detail.tmall.com/item.htm?id=533988626220&cm_id=140105335569ed55e27b&abbucket=0'
headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
print(requests.get(url, headers).text)