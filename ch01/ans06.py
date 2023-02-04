from ans05 import n_gram

def main():
    X = set(n_gram(2, "paraparaparadise"))
    Y = set(n_gram(2, "paragraph"))

    print(X | Y)
    print(X & Y)
    print(X - Y)
    print("se" in X)
    print("se" in Y)

if __name__ == "__main__":
    main()
