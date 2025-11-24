# 32. 「AのB」
# 文章textにおいて、2つの名詞が「の」で連結されている名詞句をすべて抽出せよ。

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
for i in range(len(doc) - 2):
    A = doc[i]
    NO = doc[i + 1]
    B = doc[i + 2]

    if A.pos_ == "NOUN" and NO.text == "の" and B.pos_ == "NOUN":
        print(f"{A.text}の{B.text}")

