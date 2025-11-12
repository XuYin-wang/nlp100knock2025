# 14. 1列目を出力
# ファイルの先頭10行に対して、各行の1列目だけを抜き出して表示せよ。確認にはcutコマンドなどを用いよ。

# with文でファイルを開く（ブロック終了時に自動で閉じる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
    # 表示する行数を指定（ここでは先頭10行）
    N = 10
    # リストの先頭N要素をスライスして取得し、各行を順に処理する
    for line in lines[:N]:
        # split('\t')でタブ区切りに分割し、インデックス0で1列目を取得する
        # printで取得した1列目を出力する
        print("各行の1列目だけを抜き出して表示:", line.split('\t')[0])

#実行確認$ head -n 10 popular-names.txt | cut -f1
