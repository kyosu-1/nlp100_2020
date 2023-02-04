def n_gram(n, lst) -> list:
    return [lst[i:i+n] for i in range(len(lst)-n+1)]

def main():

    sentence = "I am an NLPer"
    words = sentence.split()
    chars = list(sentence)

    print(n_gram(2, words))
    print(n_gram(2, chars))


if __name__ == "__main__":
    main()
