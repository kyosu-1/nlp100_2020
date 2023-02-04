# 各行の1列目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# uniq -c で出現頻度を求める
cut -f 1 popular-names.txt | sort | uniq -c | sort -r