# Created by Gotcha on 2017/10/9.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.corpora.wikicorpus import extract_pages,filter_wiki
import bz2file
import re
from tqdm import tqdm
import codecs
import threading

wiki = extract_pages(bz2file.open('./zhwiki-20170801-pages-articles-multistream.xml.bz2'))

def wiki_replace(d):
    s = d[1]
    s = re.sub(':*{\|[\s\S]*?\|}', '', s)
    s = re.sub('<gallery>[\s\S]*?</gallery>', '', s)
    s = re.sub('(.){{([^{}\n]*?\|[^{}\n]*?)}}', '\\1[[\\2]]', s)
    s = filter_wiki(s)
    s = re.sub('\* *\n|\'{2,}', '', s)
    s = re.sub('\n+', '\n', s)
    s = re.sub('\n[:;]|\n +', '\n', s)
    s = re.sub('\n==', '\n\n==', s)
    s = u'【' + d[0] + u'】\n' + s
    return s


def write(d):
    filename = './data/' + d[0] + '.txt'
    f = codecs.open(filename, 'w', encoding='utf-8')
    s = wiki_replace(d)
    f.write(s+'\n')
    f.close()

i = 0
j = 0
w = tqdm(wiki, desc=u'已获取0篇文章, 已处理0篇文章')
for d in w:
    about = False
    if not re.findall('^[a-zA-Z]+:', d[0]) and d[0] and not re.findall(u'^#', d[1]):
        cg_pattern = re.compile('\[\[Category:([\s\S]*)\]\]')
        categorys = cg_pattern.findall(d[1])
        j += 1
        for category in categorys:
            if category.find('金融') != -1 or category.find('經濟') != -1:
                about = True
        if about:
            th = threading.Thread(target=write, args=(d, ))
            th.start();
            i += 1
        if j % 100 == 0 :
            w.set_description(u'已获取%s篇文章, 已处理%s篇文章'%(i,j))