# -*- coding: utf-8 -*-

from collections import Counter




def getKeyWordsCount (list_data):
    total_keywords = []
    for data in list_data:
        keywords = data.description.split()  
        formatted_keywords = []
        for kw in keywords:
            kw = kw.replace(".", "")
            kw = kw.replace(",", "")
            kw = kw.replace("(", "")
            kw = kw.replace("\\", "")
            kw = kw.replace(")", "")
            kw = kw.replace(":", "")
            kw = kw.lower()
            formatted_keywords.append(kw)
        total_keywords.extend(formatted_keywords)
    print(total_keywords)
    c = Counter(total_keywords)
    print(c)


def contarFrase (buzzwords, list_data):
    
    for data in list_data:
        for bw in buzzwords:
            desc = data.description.lower()
            buzzwords[bw] += desc.count(bw.lower())
    
    return buzzwords