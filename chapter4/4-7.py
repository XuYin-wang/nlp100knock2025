
# 37. 名詞の出現頻度
# コーパスにおける名詞の出現頻度を求め、出現頻度の高い20語とその出現頻度を表示せよ。

import gzip
import json
import re
from collections import Counter


# ファイルの読み込み
texts = []
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        texts.append(data["text"])

# マークアップの除去
def clean_wiki(text):
    text = re.sub(r"\{\{.*?\}\}", "", text)
    text = re.sub(r"\[\[|\]\]", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"==.*?==", "", text)
    return text

# テキストのクリーンアップ
cleaned = [clean_wiki(t) for t in texts]
# 単語の分割と頻度計算
words = re.split(r"\W+", " ".join(cleaned))
counter = Counter(words)

# 日本語名詞のみを抽出
noun_pattern = re.compile(r"^[\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF]+$")  # 漢字、ひらがな、カタカナ
nouns_counter = Counter({word: freq for word, freq in counter.items() if noun_pattern.match(word)})
for word, freq in nouns_counter.most_common(20):
    print(word, freq)