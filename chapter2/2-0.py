
#10. 行数のカウント
#ファイルの行数をカウントせよ。確認にはwcコマンドを用いよ。
with open('popular-names.txt', 'r', encoding='utf-8') as file:
    line_count = sum(1 for line in file)
print(f"ファイルの行数: {line_count}")

#実行確認$ wc -l popular-names.txt
