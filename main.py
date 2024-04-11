def print_num_words(words):
    print(f"{len(words)} words found in the document")

def sort_on(dict):
    return dict["num"]

def print_num_letters(letters):
    list = []
    for l in letters:
        d = {}
        d["name"] = l
        d["num"] = letters[l]
        list.append(d)

    list.sort(reverse=True, key=sort_on)
    for item in list:
        print(f"The '{item["name"]}' character was found {item["num"]} times")
    

def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print("--- Begin report of books/frankenstein.txt ---")
        words = file_contents.lower().split()
        print_num_words(words)

        letters = {}
        for word in words:
            for i in range(0, len(word)):
                if (word[i].isalpha()):
                    letters[word[i]] = letters.get(word[i], 0) + 1
        print_num_letters(letters)
        print("--- End report ---")

main()