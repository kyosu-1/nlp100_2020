import random


def typoglycemia(sentence: str) -> str:
    """スペース区切の単語列に対して，各単語の先頭と末尾の文字は残し，
    それ以外の文字の順序をランダムに並び替える関数
    長さが４以下の単語は並び替えない
    """
    words = sentence.split()

    def _typoglycemia(word: str) -> str:
        if len(word) <= 4:
            return word
        else:
            return word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]

    return " ".join([_typoglycemia(word) for word in words])


def main():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(sentence))


if __name__ == "__main__":
    main()
