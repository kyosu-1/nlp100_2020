# 1列目をcol1.txtに，2列目をcol2.txtに保存
cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
# デフォルトの区切り文字はタブ