from data_structures.hashtable import Hashtable
import string


def first_repeated_word(text):
    words = [word.strip(string.punctuation).lower() for word in text.split()]
    find = Hashtable()

    for word in words:
        if find.has(word):
            return word
        find.set(word, None)
