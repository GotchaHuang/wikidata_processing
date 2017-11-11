# Created by Gotcha on 2017/11/11.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
from tqdm import tqdm

title_patt = re.compile('(\D+)\d*')
with open("../aaa/zxcdsa5542_result.json", encoding="utf-8") as f:
    text = f.read()
json_obj = json.loads(text)

datas = []
format_json = dict(data=[], version="undefined")

process = tqdm(json_obj, desc="n paras done")
count = 0
for obj in process:
    # initial
    answer = dict(answer_start="", text="")
    answers = []
    qa = dict(answers=answers, id="", question="")
    qas = []
    paragraph = dict(context="", qas=qas)
    paragraphs = []
    data = dict(paragraphs=paragraphs, title="")

    # format
    answer['answer_start'] = obj['answer'][0]
    answer['text'] = obj['answer']
    for j in range(3):
        answers.append(answer)

    qa['answers'] = answers
    qa['question'] = obj['question']
    qa['id'] = obj['id']
    qas.append(qa)

    context = obj['paragraph']
    paragraph['context'] = context
    paragraph['qas'] = qas

    title_str = title_patt.findall(obj['paragraph_id'])
    if not title_str:
        title = obj['paragraph_id']
    else:
        title = title_str[0]

    has_title = False
    has_qa = False
    for d in datas:
        if title == d['title']:
            for p in d['paragraphs']:
                if p['context'] == context:
                    p['qas'].append(qa)
                    has_qa = True
                    break
            if not has_qa:
                d['paragraphs'].append(paragraph)
                has_title = True
                break

    if not has_title:
        paragraphs.append(paragraph)
        data['paragraphs'] = paragraphs
        data['title'] = title
        datas.append(data)

    count += 1
    process.set_description("%d paras done"%count)

format_json['data'] = datas
result = json.dumps(format_json, indent=2, ensure_ascii=False)
with open('../aaa/zxcdsa5542_format_result.json', 'w', encoding='utf-8') as f:
    f.write(result)

