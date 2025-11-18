# 26. 強調マークアップの除去
# 25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）。

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
    infobox_pattern = re.compile(r'^\{\{基礎情報 国\n(.*?)^\}\}$', re.MULTILINE | re.DOTALL)
    field_pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?=\n\||\n$)', re.MULTILINE | re.DOTALL)
    infobox = {}
    infobox_match = infobox_pattern.search(text)
    if not infobox_match:
        return infobox
    infobox_text = infobox_match.group(1)
    # フィールド名と値を抽出し、辞書オブジェクトに格納する
    for field_match in field_pattern.finditer(infobox_text):
        field_name = field_match.group(1).strip()
        field_value = field_match.group(2).strip()
        # 強調マークアップの除去
        field_value = re.sub(r"'''''(.*?)'''''", r'\1', field_value)  # 強い強調
        field_value = re.sub(r"'''(.*?)'''", r'\1', field_value)      # 強調
        field_value = re.sub(r"''(.*?)''", r'\1', field_value)        # 弱い強調
        infobox[field_name] = field_value
    return infobox
uk_article_text = extract_uk_article('jawiki-country.json.gz')
infobox = extract_infobox(uk_article_text)
for field_name, field_value in infobox.items():
    print(f'{field_name}: {field_value}')
    