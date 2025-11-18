# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ。

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
# extract_sections 関数は、記事本文からセクション名とそのレベルを抽出する
def extract_sections(text):
    # 記事本文からセクション名とそのレベルを抽出するための正規表現パターンをコンパイルする
    section_pattern = re.compile(r'^(={2,})\s*(.+?)\s*\1$', re.MULTILINE)
    sections = []
    if not text:
        return sections
    # 正規表現パターンを使って記事本文を検索し、セクション名とそのレベルを抽出する
    for match in section_pattern.finditer(text):
        level = len(match.group(1)) - 1
        name = match.group(2)
        sections.append((level, name))
    return sections

uk_article_text = extract_uk_article('jawiki-country.json.gz')

sections = extract_sections(uk_article_text)
for level, name in sections:
    print(f'Level {level}: {name}')
