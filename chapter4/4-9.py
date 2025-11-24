# 39. Zipfの法則
# コーパスにおける単語の出現頻度順位を横軸、その出現頻度を縦軸として、両対数グラフをプロットせよ。

import json
import gzip
import re
from collections import Counter
import matplotlib.pyplot as plt
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
words = re.split(r"\W+", " ".join(cleaned))
counter = Counter(words)

# 頻度順位と頻度のリスト作成
freqs = sorted(counter.values(), reverse=True)
ranks = range(1, len(freqs) + 1)


# 両対数グラフのプロット
plt.loglog(ranks, freqs)
plt.xlabel("Rank (出現頻度順位)")
plt.ylabel("Frequency (出現頻度)")
plt.title("Zipfの法則（両対数グラフ）")
plt.grid(True)
plt.show()