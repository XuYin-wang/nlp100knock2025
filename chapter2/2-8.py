#18. 各行の1列目の文字列の出現頻度を求め、出現頻度の高い順に並べる
#1列目の文字列の出現頻度を求め、出現頻度と名前を出現頻度の多い順に並べて表示せよ。確認にはcut, uniq, sortコマンドを用いよ。
#
# ファイルを読み込みモードで開く（with文でブロック終了時に自動で閉じられる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
# 出現頻度を格納する辞書型の変数を初期化する
frequency_dict = {}
# ファイルの各行を順に処理する
for line in lines:
    # split('\t')でタブ区切りに分割し、インデックス0で1列目を取得する
    first_column = line.split('\t')[0]
    # 1列目の文字列が辞書に存在する場合は出現頻度を1増やし、存在しない場合は1で初期化する
    if first_column in frequency_dict:
        frequency_dict[first_column] += 1
    else:
        frequency_dict[first_column] = 1
# 辞書のアイテムを出現頻度の降順でソートする
sorted_frequency = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
# ソートされた出現頻度と名前を順に出力する
for name, freq in sorted_frequency:
    print(f"名前: {name}, 出現頻度: {freq}")