# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:34:57 2018

@author: Sebin
"""
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions
from ast import literal_eval
import numpy 
import pandas as pd
import wikipediaapi
dialog='I love India'



natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='YOUR USERNAME',
  password='YOUR PASSWORD',
  version='YOUR VERSION')

response = natural_language_understanding.analyze(
  text= dialog,
  language = 'en',

  features=Features(
    entities=EntitiesOptions(
      emotion=False,
      sentiment=False,
      limit=2),
    keywords=KeywordsOptions(
      emotion=False,
      sentiment=False,
      limit=2)))


#y = json.loads(response)

keywordout = response['keywords']
wiki_wiki = wikipediaapi.Wikipedia('en')
for f in keywordout:
    entities = f['text']
    
#    entities = response['keywords'][1]['text']
    page_py = wiki_wiki.page(entities)
    print(f)
    print(page_py.summary[0:200]+"...")
#    print("Click here>> " + page_py.fullurl)
#    print()

