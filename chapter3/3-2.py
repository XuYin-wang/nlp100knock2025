# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ。

import json
import gzip
# extract_category_names 関数は、指定された国の記事からカテゴリ名を抽出する
def extract_category_names(file_path, country_title):
    category_names = []
    # 指定された国の記事からカテゴリ名を抽出する、'rt'モードでgzipファイルを開き、utf-8エンコーディングを指定する
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            # ファイルを1行ずつ読み込み、JSON形式の文字列をPythonの辞書オブジェクトに変換する
            article = json.loads(line)
            if article['title'] == country_title:
                # 記事本文を行ごとに分割し、カテゴリ名を抽出する
                for text_line in article['text'].split('\n'):
                    # 各行がカテゴリ名の形式かどうかを確認する
                    if text_line.startswith('[[Category:'):
                        # カテゴリ名を抽出し、リストに追加する
                        category_name = text_line[len('[[Category:'): -2]
                        # 抽出したカテゴリ名をリストに追加する
                        category_names.append(category_name)
                break
    return category_names
category_names = extract_category_names('jawiki-country.json.gz', 'イギリス')
for name in category_names:
    print(name)