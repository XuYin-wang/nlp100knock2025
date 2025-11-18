# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し、辞書オブジェクトとして格納せよ。

import re
import gzip
import json
def extract_uk_article(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            article = json.loads(line)
            if article.get('title') == 'イギリス':
                return article.get('text', '')
# extract_infobox 関数は、記事本文から基礎情報テンプレートを抽出する
def extract_infobox(text):
        # 基礎情報テンプレートの開始と終了を検出するための正規表現パターンをコンパイルする
    infobox_pattern = re.compile(r'^\{\{基礎情報 国\n(.*?)^\}\}$', re.MULTILINE | re.DOTALL)
        # フィールド名と値を抽出するための正規表現パターンをコンパイルする
    field_pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?=\n\||\n$)', re.MULTILINE | re.DOTALL)
    infobox = {}
    # 基礎情報テンプレートの開始と終了を検出する
    infobox_match = infobox_pattern.search(text)
    if not infobox_match:
        return infobox
    # 基礎情報テンプレートの内容を取得する
    infobox_text = infobox_match.group(1)
    # フィールド名と値を抽出し、辞書オブジェクトに格納する
    for field_match in field_pattern.finditer(infobox_text):
        field_name = field_match.group(1).strip()
        field_value = field_match.group(2).strip()
        infobox[field_name] = field_value
    return infobox
# 関数を呼び出して結果を表示する
uk_article_text = extract_uk_article('jawiki-country.json.gz')
# 抽出した基礎情報テンプレートのフィールド名と値を表示する
infobox = extract_infobox(uk_article_text)
# 抽出した基礎情報テンプレートのフィールド名と値を表示する
for field_name, field_value in infobox.items():
    print(f'{field_name}: {field_value}')