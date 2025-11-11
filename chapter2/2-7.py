# 17. １列目の文字列の異なり
# 1列目の文字列の異なり（文字列の種類）を求めよ。確認にはcut, sort, uniqコマンドを用いよ。

# ファイルを読み込みモードで開く（with文でブロック終了時に自動で閉じられる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()

# 重複なしの要素を格納するセット型の変数を初期化する
unique_first_column = set()

# ファイルの各行を順に処理する
for line in lines:
    # split('\t')でタブ区切りに分割し、インデックス0で1列目を取得する
    first_column = line.split('\t')[0]
    # セットに1列目の文字列を追加する（重複は自動で除外される）
    unique_first_column.add(first_column)

# len()でセットの要素数（異なる1列目の文字列の種類数）を取得して出力する
print("異なる1列目の文字列の種類数:", len(unique_first_column))