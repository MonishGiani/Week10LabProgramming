def find_linking_subword(word1, word2):
    min_len = min(len(word1), len(word2))
    for i in range(min_len, 0, -1):
        if word1.endswith(word2[:i]):
            return word2[:i]
    return None

def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    linking_subword = find_linking_subword(word1, word2)

    if linking_subword:
        print(f"Both words can be linked with the subword '{linking_subword}'.")
    else:
        print("Both words cannot be linked.")

if __name__ == "__main__":
    main()
