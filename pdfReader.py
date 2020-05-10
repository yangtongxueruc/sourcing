#-*- conding: utf-8 -*-

import pdfplumber

with pdfplumber.open('read.pdf') as pdf:
    content = ''
    print(len(pdf.pages)) #为PDF文档页数
    for i in range(len(pdf.pages)):
    	#pdf.pages[i] 是读取PDF文档第i+1页
        page = pdf.pages[i]
        #page.extract_text()函数即读取文本内容，下面这步是去掉文档最下面的页码
        page_content = '\n'.join(page.extract_text().split('\n')[:-1])
        content = content + page_content
    need = content.split('成绩')[1].split('公示期内')[0]
    print(need)
    print(type(need))