# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7
#爬取“BTKitty”的磁力链接，并保存到exls文件中。
#2.0版本增加了对多个关键词的搜索
# 关键词的获取需要登录网站，从地址栏中获取。

import requests
from bs4 import BeautifulSoup
import os
import re
import xlwt
import time
import datetime
ver=datetime.datetime.now().strftime('%Y%m%d')

print "本程序可以爬取“BTKitty”中的磁力链接，并保存为excel文档。"
keyWds={'高清':'U3q5esazHa1KAA','高跟':'U3q5esaL7fOVAA','制服':'U3rase3ZnF4lAA','丝袜':'U3qyY-6LRXOUAA','国产':'U3o6e--TXcuVAA'}
keys=""
for keyWd in keyWds.keys():
    keys=str(keyWd)+" "+keys
print "当前爬取的关键字包括："+keys+"\n**********\n"
j=1
book = xlwt.Workbook(encoding='utf-8',style_compression=0)  #使用workbook方法，创建一个新的工作簿
sheet = book.add_sheet("BTKitty",cell_overwrite_ok=True)    #添加一个sheet，名字为"BTKitty"，参数overwrite就是说可不可以重复写入值，就是当单元格已经非空，你还要写入
biaotoulist=["关键词","序号","文件名","收录时间","文件大小","文件数","速度","人气","磁力链"] #编辑表头
for k in range(9):
    sheet.write(0,k,list(biaotoulist)[k])
    book.save(u"BTKitty链接"+str(ver)+".xls")
# 设置报头,Http协议,增加参数Refer对付防盗链设置
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36','Referer': "http:://http://www.mzitu.com/"}
parser = 'html.parser'    
for keyWd in dict(keyWds).keys():
    print "开始提取关键字："+keyWd   
    for i in range(2):
        url_keyWd=keyWds[keyWd]
        url = "http://cnbtkitty.com/search/"+url_keyWd+"/" + str(i+1) + "/1/0.html"  # 爬取目标
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
            sheet.write(j,8,mag_link)
            sheet.write(j,2,mag_title)
            sheet.write(j,1,str(j))
            sheet.write(j,0,keyWd)
            for l in range(5):
                sheet.write(j,l+3,str(list(mag_attr)[l].text))
            book.save(u"BTKitty链接"+str(ver)+".xls")
            j=j+1
        print ("第"+str(i+1)+"页提取完成！")
    print ("累计提取"+str(j-1)+"项记录。")
    print "********************"+"\n"



