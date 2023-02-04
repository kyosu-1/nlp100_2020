# ファイルをN分割する
# Usage: bash ans16.sh [N]
N=$1
split -l $(( $(wc -l < popular-names.txt) / $N )) popular-names.txt