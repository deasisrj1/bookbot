def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    letter_count = count_letters(text)
    sorted_count = get_sorted(letter_count)
    print_sorted_count(sorted_count)
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def sort_on(f):
    print(f[1])
    return f[1]

def get_sorted(dict_char):
    out = []
    for char in dict_char:
        if char.isalpha():
            out.append((char, dict_char[char]))
    out.sort(key = lambda c: c[1], reverse=True)
    
    return out

def print_sorted_count(sorted_count):
    for char in sorted_count:
        print(f"The '{char[0]}' character was found {char[1]} times")

main()