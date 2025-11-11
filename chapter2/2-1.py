# 11. 先頭からN行を出力
# ファイルの先頭N行だけを表示せよ。例えば、N=10として先頭10行を表示せよ。確認にはheadコマンドを用いよ。

# 'with'文でファイルを開くと、ブロック終了時に自動でファイルが閉じられる
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
    # 表示する行数を指定（ここでは10行）
    N = 10
    # リストの先頭N要素をスライスして取得する
    for line in lines[:N]:
        # rstrip()で行末の改行を削除してから表示する
        print("ファイルの先頭N行だけを表示:", line.rstrip())