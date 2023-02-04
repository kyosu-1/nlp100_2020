# popular-name.txtの1列目の異なる文字列の集合を求める
# 1列目を抽出してソートして重複を削除する
cut -f 1 popular-names.txt | sort | uniq