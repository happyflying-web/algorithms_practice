import re
import time
import pandas as pd

import requests
from urllib import parse
from selenium import webdriver

url = "https://www.aqistudy.cn/historydata/"
url_text = requests.get(url).text

pattern =  re.compile(r'<a href="monthdata.php\?city=\w+">(\w+)</a>\r\n') # 要在?前加\转义符
citys = pattern.findall(url_text) # 获取384个城市名
print("已获取{}个城市名，第一个城市是{}，最后一个城市是{}".format(len(citys),citys[0],citys[-1]))

base_url = 'https://www.aqistudy.cn/historydata/monthdata.php?city='
driver = webdriver.PhantomJS(r'E:\newsoftwareinstall\phantomjs-2.1.1-windows\bin\phantomjs.exe')

for i,city in enumerate(citys):
    city_url = base_url + parse.quote(city)
    driver.get(city_url)
    time.sleep(2)
    dataframe = pd.read_html(driver.page_source)[0]
    time.sleep(1)
    dataframe.to_csv(r'E:\\newsoftwareinstall\\空气污染月数据\\%s.csv'% (str(city)),mode='a+',encoding='utf_8_sig')
    print("第{}个城市：{} 已收集完".format(i+1,city))
driver.quit()
print('已收集完！')
