import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.findall(r'\b\w+\b', sentence.lower())
word_lengths = [len(word) for word in words]
print(word_lengths)
