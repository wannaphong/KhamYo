# -*- coding: utf-8 -*-
import itertools
import copy
import os
import json
from collections import defaultdict
from sentence_transformers import SentenceTransformer, util
import numpy as np
from pythainlp.tokenize import Tokenizer
from pythainlp.corpus import thai_words
from khamyo import __file__ as khamyo_file

path_file = os.path.join(os.path.dirname(khamyo_file),'data.json')

model = SentenceTransformer('airesearch/wangchanberta-base-att-spm-uncased')

with open(path_file, encoding='utf-8') as fh:
    worddict = json.load(fh)

list_th = list(worddict.keys())
tokenizer = Tokenizer(list_th+list(thai_words()), engine='newmm', keep_whitespace="False")


def merge(l: list) -> list:
  list_sent = []
  temp = ""
  for i in l:
    if i not in list_th:
      temp += i
    elif temp!="":
      list_sent.append(temp)
      list_sent.append(i)
      temp = ""
    else:
      list_sent.append(i)
  if temp!="":
    list_sent.append(temp)
  return list_sent


def counts(l: list) -> defaultdict:
  _temp = defaultdict(int)
  for i in l:
    if i in list_th:
      _temp[i]+=1
  return _temp


def replace(sentence: str, top_k: int = 2) -> list:
  sent_words = tokenizer.word_tokenize(sentence)
  c = counts(sent_words)
  if c == {}:
    return [(sentence,None)]
  del c
  list_index = []
  list_temp = []
  j = 0
  for i,w in enumerate(sent_words):
    if w in list_th:
      if len(worddict[w])>1:
        list_index.append(i)
        list_temp.append(worddict[w])
      else:
        sent_words[i] = worddict[w][0]
  sum_m = list(itertools.product(*list_temp))
  list_sent = []
  sentence_embedding = model.encode(sentence, convert_to_tensor=True)
  for i,v in enumerate(sum_m):
    _t = copy.copy(sent_words)
    for j,w in enumerate(v):
      _t[list_index[j]] = w
    list_sent.append(''.join(_t))
  if len(sum_m) == 1:
      s2 = model.encode(list_sent[0], convert_to_tensor=True)
      return [(list_sent[0],util.pytorch_cos_sim(sentence_embedding,s2))]
  corpus_embeddings = model.encode(list_sent, convert_to_tensor=True)
  cos_scores = util.pytorch_cos_sim(sentence_embedding, corpus_embeddings)[0]
  top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
  return [(list_sent[i], cos_scores[i]) for i in top_results[0:top_k].tolist()]
