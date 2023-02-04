def cipher(text: str) -> str:
    return "".join([chr(219 - ord(c)) if c.islower() else c for c in text])


def main():
    text = "I am an NLPer"
    print(cipher(text))
    print(cipher(cipher(text)))


if __name__ == "__main__":
    main()
