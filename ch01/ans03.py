import re


def word_character_counts_list(s: str) -> list[str]:
    """
    英文を単語に分解し、各単語の文字数をリストにして返す
    """
    # 正規表現で,と.を除去
    s = re.sub('[,\.]', '', s)
    return [len(word) for word in s.split()]

if __name__ == "__main__":
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(word_character_counts_list(s))
