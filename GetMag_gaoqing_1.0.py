# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7
#爬取“BTKitty”的磁力链接，并保存到exls文件中。


import requests
from bs4 import BeautifulSoup
import os
import re
import xlwt
import time
import datetime
ver=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

print "本程序可以爬取“BTKitty”中的磁力链接，并保存为excel文档。"
print "本程序关键词为“高清”。"
print "********************"
print

#使用workbook方法，创建一个新的工作簿
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#添加一个sheet，名字为mysheet，参数overwrite就是说可不可以重复写入值，就是当单元格已经非空，你还要写入
sheet = book.add_sheet('高清',cell_overwrite_ok=True)
biaotoulist=["序号","文件名","收录时间","文件大小","文件数","速度","人气","磁力链"]
for k in range(8):
    sheet.write(0,k,list(biaotoulist)[k])
    book.save(u"高清"+str(ver)+".xls")


# 设置报头,Http协议,增加参数Refer对付防盗链设置
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36','Referer': "http:://http://www.mzitu.com/"}
parser = 'html.parser'
j=1
for i in range(2):
    url = "http://cnbtkitty.com/search/U3q5esazHa1KAA/" + str(i+1) + "/1/0.html"  # 爬取目标
    cur_page = requests.get(url, headers=header)
    soup = BeautifulSoup(cur_page.text, parser)
    mag_tag=soup.find("title").string
    mag_tag=list(re.split(u'"|',mag_tag))[1]  #提取关键词
    mag_cont_list=soup.find_all(attrs={'class':'list-con'})
    for mag_cont in mag_cont_list:
        mag_title=mag_cont.find("a").text
        mag_title=mag_title.replace(".torrent","")
        mag_link=mag_cont.find(attrs={'class':'option'}).find('a')['href']
        mag_attr=mag_cont.find(attrs={'class':'option'}).find_all('b')
        sheet.write(j,7,mag_link)
        sheet.write(j,1,mag_title)
        sheet.write(j,0,str(j))
        for l in range(5):
            sheet.write(j,l+2,str(list(mag_attr)[l].text))
        book.save(u"高清"+str(ver)+".xls")
        j=j+1
    print ("第"+str(i+1)+"页提取完成！")
print ("共提取"+str(i+1)+"页，共提取"+str(j-1)+"项记录。")


