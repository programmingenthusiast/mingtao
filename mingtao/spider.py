#!/usr/bin/python
# Filename: spider.py

#encoding:utf-8
import time
import urllib2
import re
import os
from bs4 import BeautifulSoup

url='https://www.zhihu.com/question/40753170'
urlop = urllib2.urlopen(url) # python 2.7 has no urllib.request.urlopen()
data = urlop.read().decode('utf-8')
bs = BeautifulSoup(data)

def gettitle(url):
    title = bs.find('span', {"class":"zm-editable-content"}) # findout title
    title = title.get_text()
    return(title)

def getpicurl(url): # get pic url
    pics = re.compile('img.+?src=\"(https.+?)\"')
    return(pics)

def downpics():
    title = gettitle(url)
    print title
    dirpath='d:/pict/'
    if not os.path.exists(dirpath):
        os.makedirs(dirpath) # to generate folder saving pics
    pics = getpicurl(url)
    a = 1
    urls = []

    for x in pics.findall(data): # remove duplicated pic url
        if x not in urls:
            urls.append(x)
        print urls

    for x in urls:
        try:
            print '==url==', x
            imagdata = urllib2.urlopen(x).read()
            print '==imagedata==', imagdata
            b = (x.rfind("."))
            print '==b==', b
            imgpath = str(dirpath) + str(a) + x[b:]
            print '==imgpath', imgpath
            a += 1
            file = open(imgpath,'wb')
            file.write(imagdata)
            file.flush()
            file.close()
        except:
            continue
        
        if a == 20:
            break
        
downpics();
