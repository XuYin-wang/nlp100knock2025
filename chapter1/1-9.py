import random

def shuffle_word(word):
    if len(word) <= 4:
        return word
    else:
        first = word[0]
        last = word[-1]
        middle = list(word[1:-1])
        random.shuffle(middle)
        return first + "".join(middle) + last

def typoglycemia(sentence):
    words = sentence.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return " ".join(shuffled_words)

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
shuffled_sentence = typoglycemia(sentence)
print(shuffled_sentence)
