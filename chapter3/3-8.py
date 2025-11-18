# 28. MediaWikiマークアップの除去
# 27の処理に加えて、テンプレートの値からMediaWikiマークアップを可能な限り除去し、国の基本情報を整形せよ。

import re
import gzip
import json
def extract_uk_article(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            article = json.loads(line)
            if article.get('title') == 'イギリス':
                return article.get('text', '')
def extract_infobox(text): 
    infobox_pattern = re.compile(r'^\{\{基礎情報 国\n(.*?)^\}\}$', re.MULTILINE | re.DOTALL)
    field_pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?=\n\||\n$)', re.MULTILINE | re.DOTALL)
    infobox = {}
    infobox_match = infobox_pattern.search(text)
    if not infobox_match:
        return infobox
    infobox_text = infobox_match.group(1)
    for field_match in field_pattern.finditer(infobox_text):
        field_name = field_match.group(1).strip()
        field_value = field_match.group(2).strip()
        # 強調マークアップの除去
        field_value = re.sub(r"'''''(.*?)'''''", r'\1', field_value)  # 強い強調
        field_value = re.sub(r"'''(.*?)'''", r'\1', field_value)      # 強調
        field_value = re.sub(r"''(.*?)''", r'\1', field_value)        # 弱い強調
        # 内部リンクマークアップの除去
        field_value = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', field_value)
        # 外部リンクマークアップの除去
        field_value = re.sub(r'\[http[^\s]*\s?(.*?)\]', r'\1', field_value)
        # HTMLタグの除去
        field_value = re.sub(r'<.*?>', '', field_value)
        # その他のマークアップの除去（例: 改行、脚注など）
        field_value = re.sub(r'<ref.*?>.*?</ref>', '', field_value, flags=re.DOTALL)  # 脚注
        field_value = re.sub(r'\n', ' ', field_value)  # 改行をスペースに置換
        infobox[field_name] = field_value.strip()
    return infobox
uk_article_text = extract_uk_article('jawiki-country.json.gz')
infobox = extract_infobox(uk_article_text)
for field_name, field_value in infobox.items():
    print(f'{field_name}: {field_value}')