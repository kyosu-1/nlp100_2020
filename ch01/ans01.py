s = "stredded"
print(s[::-1])

# スライスは[start:stop:end]の形で範囲や増分を指定する
# start, stopを省略すると全体を選択し、stepを-1とすると後ろから一つずつ要素を取得することになる
# [::-1]とすると逆順に並べ替えられたオブジェクトが取得できる。