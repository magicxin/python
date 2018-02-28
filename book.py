#encoding:utf8

import re

import urllib2

url = 'http://www.23us.com/html/55/55304/'

request = urllib2.Request(url)

response = urllib2.urlopen(request)

content = response.read().decode('gbk')

the_url = re.compile('<td class=\"L"\><a href=\"(.*?)"\>.*?</a></td>',re.S)

last_url = the_url.findall(content)

for i in last_url:

    print i

    url = 'http://www.23us.com/html/55/55304/'+i

    request = urllib2.Request(url)

    response = urllib2.urlopen(request)

    zhi = response.read()

    code = re.compile('.*?content="text.html; charset=(.*?)".*?',re.S)

    last_code = code.findall(zhi)[0]

    try:

        content = zhi.decode(''+last_code)

    except:

        try:

            content = zhi.decode('gb2312')

        except:

            continue

    last_content = re.compile('<title>(.*?)</title>.*?<dd id="contents">(.*?)</dd>',re.S)

    last_content = last_content.findall(content)    

    if last_content==[]:        

            print '采集失败'

            print content

    for I,J in last_content:

        J = J.replace('&nbsp;','').replace('<br/> <br/>','\n')  

        file = open('小说.txt','a+')

        t = '\n\n\t\t' + I + '\n\n' + '\t' + J

        file.write(t.encode('utf-8'))        

        file.close()