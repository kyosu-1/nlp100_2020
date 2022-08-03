prev = "パトカー"
next = "タクシー"

# 先頭から文字列を交互に結合
def join_alternately(prev: str, next: str) -> str:
    """先頭から文字列を交互に結合

    Args:
        prev (str): 前の文字列
        next (str): 次の文字列

    Raises:
        ValueError: 文字列の長さが異なる

    Returns:
        str: 交互に結合した文字列
    """
    if len(prev) != len(next):
        raise ValueError("文字列の長さが異なります")
    return "".join([i + j for i, j in zip(prev, next)])

print(join_alternately(prev, next))
# ->  パタトクカシーー
