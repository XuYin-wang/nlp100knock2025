

# 31. 動詞の原型
# 文章textに含まれる動詞と、その原型をすべて表示せよ。

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
    if token.pos_ == "VERB":
        print(f"{token.lemma_}")