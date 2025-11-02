def cipher(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_char_code = 219 - ord(char)
            result += chr(new_char_code)
        else:
            result += char
    return result

print("文字列を入力：")
char = input()
print(cipher(char))
