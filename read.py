from collections import Counter
from string import punctuation

def word_count(text):
    """return dict containing counts of each word"""
    for char in punctuation:
        text = text.replace(char, "")

    text = text.lower()

    return Counter(text.split(" "))

def read_book(path):
    """opens a book and returns text as string"""
    with open(path, "r") as f:
        b = f.read()
        text = b.replace("\r", "")

    return " ".join(text.split())

def word_stats(text):
    """returns: number of unique words, count of each word occurrences"""
    words = word_count(text)
    count = words.values()
    unique = len(words)

    return (unique, count)


