# 16. ランダムに各行を並び替える
# ファイルを行単位でランダムに並び替えよ（注意: 各行の内容は変更せずに並び替えよ）。同様の処理をshufコマンドで実現せよ。

# ファイルを読み込みモードで開く（with文でブロック終了時に自動で閉じられる）
with open('popular-names.txt', 'r') as f:
    # readlines()でファイル全体を行ごとのリストとして読み込む
    lines = f.readlines()

# randomモジュールをインポートする（ランダム処理に必要）
import random

# shuffle()でリストの要素をランダムに並び替える（元のリストを直接変更）
random.shuffle(lines)

# ランダムに並び替えたデータを新しいファイルに書き込む
with open('shuffled-popular-names.txt', 'w') as f:
    # writelines()でリスト内の全ての行を一度にファイルに書き込む
    f.writelines(lines)

#実行確認$ shuf popular-names.txt > shuffled-popular-names.txt
