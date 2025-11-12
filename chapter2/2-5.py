# 15. ファイルをN分割する
# ファイルを行単位でN分割し、別のファイルに格納せよ。例えば、N=10としてファイルを10分割せよ。同様の処理をsplitコマンドで実現せよ。

# 分割数を指定する
N = 10
# ファイルを読み込みモードで開く（with文でブロック終了時に自動で閉じられる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()
    # ファイルの総行数を取得する
    total_lines = len(lines)
    # 各分割ファイルに入る行数を計算する（余りがあれば切り上げ）
    lines_per_file = (total_lines + N - 1) // N

    # N個の分割ファイルを作成するためにループを回す
    for i in range(N):
        # 新しい出力ファイルを書き込みモードで開く
        with open(f'popular-names-part-{i+1}.txt', 'w') as out_f:
            # 分割ファイルの開始行インデックスを計算する
            start_index = i * lines_per_file
            # 分割ファイルの終了行インデックスを計算する（ファイル末尾を超えないように制限）
            end_index = min(start_index + lines_per_file, total_lines)
            # スライスで取得した行をループで処理する
            for line in lines[start_index:end_index]:
                # 行を出力ファイルに書き込む
                out_f.write(line)
                
#実行確認$ split -n 10 popular-names.txt popular-names-part-
