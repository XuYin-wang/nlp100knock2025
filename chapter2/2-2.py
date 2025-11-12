# 12. 末尾のN行を出力
# ファイルの末尾N行だけを表示せよ。例えば、N=10として末尾10行を表示せよ。確認にはtailコマンドを用いよ。

# ファイルを読み込みモードで開き、ブロック終了時に自動で閉じる（with文）
with open ('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
    # 表示する行数を指定（ここでは10行）
    N = 10
    # リストの末尾N要素をスライスして取得し、各行を出力する
    for line in lines[-N:]:
        # rstrip()で行末の改行を削除してから表示する
        print("ファイルの末尾N行だけを表示:", line.rstrip())

#実行確認$ tail -n 10 popular-names.txt
