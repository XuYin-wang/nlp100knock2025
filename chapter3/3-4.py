# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ。

import re
import gzip
import json
# extract_uk_article 関数は、指定された国の記事本文を抽出する
def extract_uk_article(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            article = json.loads(line)
            if article.get('title') == 'イギリス':
                return article.get('text', '') 
# extract_media_files 関数は、記事本文からメディアファイル名を抽出する
def extract_media_files(text):
    # 記事本文からメディアファイル名を抽出するための正規表現パターンをコンパイルする
    media_pattern = re.compile(r'\[\[ファイル:(.+?)(\|.*?)*\]\]')
    # 正規表現パターンを使って記事本文を検索し、メディアファイル名を抽出する
    media_files = media_pattern.findall(text)
    return [match[0] for match in media_files]
uk_article_text = extract_uk_article('jawiki-country.json.gz')
# 抽出したメディアファイル名を表示する
media_files = extract_media_files(uk_article_text)
for media_file in media_files:
    print(media_file)