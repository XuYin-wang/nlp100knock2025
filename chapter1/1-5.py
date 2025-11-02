def n_grams(sequence, n):
    ngrams = []
    for i in range(len(sequence) - n + 1):
        ngrams.append(sequence[i : i + n])
    return ngrams

sentence = "I am an NLPer"

char_trigrams = n_grams(sentence, 3)
print("tri-grams:", char_trigrams)

words = sentence.split()
word_bigrams = n_grams(words, 2)
print("bi-grams:", word_bigrams)
