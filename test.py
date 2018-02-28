#!/usr/bin/python
#coding=utf-8 

'''
python多行注释略显奇怪
'''
content = "老饼出现在了脚本中!"
content_unicode = content.decode("utf-8")
content_gbk = content_unicode.encode("gbk")
print content_gbk; 

raw = "按下 enter 键退出，其他任意键显示...\n"
raw_unicode = raw.decode("utf-8")
raw_gbk = raw_unicode.encode("gbk")
raw_input(raw_gbk)