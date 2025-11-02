import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = re.findall(r'\b\w+\b', sentence)
result_dict = {}
one_char_idx = {1, 5, 6, 7, 8, 9, 15, 16, 19}

for i, word in enumerate(words, 1):
    if i in one_char_idx:
        result_dict[word[0]] = i
    else:
        result_dict[word[:2]] = i

print(result_dict)
