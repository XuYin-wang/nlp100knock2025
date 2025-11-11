# 13. タブをスペースに置換
# ファイルの先頭10行に対して、タブ1文字につきスペース1文字に置換して出力する

# with文でファイルを開く（ブロック終了時に自動で閉じる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
    # 表示する行数を指定（ここでは先頭10行）
    N = 10
    # リストの先頭N要素をスライスして取得し、各行を順に処理する
    for line in lines[:N]:
        # replace()でタブ('\t')をスペース(' ')に置換する
        # printのend=''で既存の行末改行を重複させない
        print(line.replace('\t', ' '), end='')
