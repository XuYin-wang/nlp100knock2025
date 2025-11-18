# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ。

import gzip
import json
# extract_category_lines 関数は、指定された国の記事からカテゴリ名を含む行を抽出する
def extract_category_lines(file_path, country_title):
    category_lines = []
    # 指定された国の記事からカテゴリ名を含む行を抽出する
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            # ファイルを1行ずつ読み込み、JSON形式の文字列をPythonの辞書オブジェクトに変換する
            article = json.loads(line)
            # 指定された国の記事タイトルと一致するか確認する、そして記事本文を行ごとに分割する
            if article['title'] == country_title:
                # 記事本文を行ごとに分割し、カテゴリ名を含む行を抽出する
                for text_line in article['text'].split('\n'):
                    if 'Category:' in text_line:
                        category_lines.append(text_line)
                break
    return category_lines
category_lines = extract_category_lines('jawiki-country.json.gz', 'イギリス')
for line in category_lines:
    print(line) 