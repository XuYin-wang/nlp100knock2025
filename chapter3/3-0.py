# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある。

# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が"title"キーに、記事本文が"text"キーの辞書オブジェクトに格納され、そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ。

# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み、「イギリス」に関する記事本文を表示せよ。問題21-29では、ここで抽出した記事本文に対して実行せよ。

import gzip
import json
# extract the article 関数は、指定された国の記事本文を抽出する
def extract_uk_article(file_path):
    # gzipで圧縮されたファイルを開き、テキストモードで読み込み、エンコーディングをutf-8に指定する。for line in fでファイルを1行ずつ読み込む
    # 各行をjson.loadsでJSON形式の文字列からPythonの辞書オブジェクトに変換する
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            # 各行のJSONデータを解析する
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']
# 関数を呼び出して結果を表示する。uk_article_text変数に抽出した記事本文を格納し、出力する
uk_article_text = extract_uk_article('jawiki-country.json.gz')
print(uk_article_text)
