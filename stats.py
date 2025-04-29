def get_number_of_words(content):
    return len(content.split())

def get_letter_count(content):
    chars = {}
    for c in content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def organize_sets(chars):
    organized_dict = []
    for char in chars:
        organized_dict.append({"letter": char, "count": chars[char]})
    return organized_dict

def pretty_print(book_path, words, chars):
    organized_chars = organize_sets(chars)
    organized_chars.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in organized_chars:
        if char["letter"].isalpha():
            print(f"{char["letter"]}: {char["count"]}")
    print("============= END ===============")