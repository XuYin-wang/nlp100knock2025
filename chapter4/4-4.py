# 34. 主述の関係
# 文章textにおいて、「メロス」が主語であるときの述語を抽出せよ。

import spacy
import ginza
nlp = spacy.load("ja_ginza")

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

doc = nlp(text)
for token in doc:
    if token.dep_ == "nsubj" and token.text == "メロス":
        print(token.head.text)