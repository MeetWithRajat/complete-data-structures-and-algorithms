"""1. Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
Output:
{'apple': 3, 'orange': 2, 'banana': 1}"""


def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


word_list = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(word_list))

"""2. Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:
{'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
