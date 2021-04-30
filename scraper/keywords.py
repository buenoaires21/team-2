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


def contarFrase (frase, list_data):
    merged_desc = ""
    for data in list_data:
        merged_desc += " " + data.description.lower()
    c = merged_desc.count(frase)
    return c