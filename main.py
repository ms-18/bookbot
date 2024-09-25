def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for key, value in char_count.items():
        print(f"The '{key}' character was found {value} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text: str):
    text = text.lower()
    count_dict = {}
    for charcter in text:
        count = count_dict.get(charcter, 0)
        count_dict[charcter] = count + 1
    return count_dict
    
        
main()