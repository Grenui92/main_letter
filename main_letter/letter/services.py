import re

def search_letter(text):
    words = re.findall(r'\b\w+', text)

    letters_list = []
    for word in words:
        letters_list.append(search_first_unique_letter(word))

    return search_first_unique_letter(letters_list)

def search_first_unique_letter(word):
    for letter in word:
        if word.count(letter) == 1:
            return letter