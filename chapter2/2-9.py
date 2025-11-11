#19. 3列目の数値の降順に各行を並び替える
#3列目の数値の逆順でファイルの各行を整列せよ（注意: 各行の内容は変更せずに並び替えよ）。同様の処理をsortコマンドで実現せよ。

# ファイルを読み込みモードで開く（with文でブロック終了時に自動で閉じられる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
# sort()で3列目の数値を基準に降順で並び替える（元のリストを直接変更）
lines.sort(key=lambda line: int(line.split('\t')[2]), reverse=True)
# 並び替えた各行を順に出力する
for line in lines:
    print(line.rstrip())    