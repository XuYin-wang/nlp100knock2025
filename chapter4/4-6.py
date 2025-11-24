# 36. 単語の出現頻度
# 問題36から39までは、Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzをコーパスと見なし、統計的な分析を行う。
# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が"title"キーに、記事本文が"text"キーの辞書オブジェクトに格納され、そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される
# まず、Wikipedia記事からマークアップを除去し、各記事のテキストを抽出せよ。そして、コーパスにおける単語（形態素）の出現頻度を求め、出現頻度の高い20語とその出現頻度を表示せよ。

import gzip
import json
import re
from collections import Counter
#　ファイルの読み込み
texts = []
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        texts.append(data["text"])

# マークアップの除去
def clean_wiki(text):
    text = re.sub(r"\{\{.*?\}\}", "", text)      # {{ ... }}
    text = re.sub(r"\[\[|\]\]", "", text)        # [[ ]]]
    text = re.sub(r"<.*?>", "", text)            # <ref>...</ref> 等
    text = re.sub(r"==.*?==", "", text)          # 标题
    return text
# テキストのクリーンアップ
cleaned = [clean_wiki(t) for t in texts]

# 単語の分割と頻度計算
words = re.split(r"\W+", " ".join(cleaned))
counter = Counter(words)

for word, freq in counter.most_common(20):
    print(word, freq)
