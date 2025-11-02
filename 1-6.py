def char_bigrams(text):
    bigrams = set()
    for i in range(len(text) - 1):
        bigrams.add(text[i:i+2])
    return bigrams

text1 = "paraparaparadise"
text2 = "paragraph"

X = char_bigrams(text1)
Y = char_bigrams(text2)

union = X | Y
intersection_xy = X & Y
difference_x_y = X - Y

print(f"Xのbi-gram: '{text1}': {X}")
print(f"Yのbi-gram: '{text2}': {Y}")
print(f"和集合: {union}")
print(f"積集合: {intersection_xy}")
print(f"差集合: {difference_x_y}")

se_in_X = 'se' in X
se_in_Y = 'se' in Y

print(f"'se' in X: {se_in_X}")
print(f"'se' in Y: {se_in_Y}")
