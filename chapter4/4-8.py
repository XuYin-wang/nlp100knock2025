# 38. TF・IDF
# 日本に関する記事における名詞のTF・IDFスコアを求め、TF・IDFスコア上位20語とそのTF, IDF, TF・IDFを表示せよ。

import json
import gzip
import re
from collections import Counter
import math
# ファイルの読み込み
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
words = [re.split(r"\W+", t) for t in cleaned]
# 日本語名詞のみを抽出
noun_pattern = re.compile(r"^[\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF]+$")  # 漢字、ひらがな、カタカナ
def get_nouns(text):
    words = re.split(r"\W+", text)
    return [w for w in words if noun_pattern.match(w)]

docs = [get_nouns(t) for t in cleaned]

# 4. TF（全文章合計）
tf = Counter()
for doc in docs:
    tf.update(doc)

# 5. IDF（日本関連記事の中で何文書に出たか）

N = len(docs)
df = Counter()

for doc in docs:
    for w in set(doc):
        df[w] += 1

idf = {w: math.log(N / df[w]) for w in df}

# 6. TF-IDF 計算
tfidf = {w: tf[w] * idf[w] for w in tf}

# 7. 上位20語
top20 = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:20]

print("語\tTF\tIDF\tTF・IDF")
for w, score in top20:
    print(f"{w}\t{tf[w]}\t{idf[w]:.4f}\t{score:.4f}")