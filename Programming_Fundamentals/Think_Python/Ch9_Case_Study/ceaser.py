def rotate_word(word, number):
    try:
        str(word)
        number = int(number)
    except:
        print("we require a word and a number")

    newword = []
    for letter in word:
        if letter.isupper():
            letter = ((ord(letter) - 64) + number) % 26
            letter = chr(letter + 64)
            newword.append(letter)
        if letter.islower():
            letter = ((ord(letter) - 97) + number) % 26
            letter = chr(letter + 97)
            newword.append(letter)
    return "".join(newword)


p = ((ord('A') - 64) + 29) % 26

print(rotate_word('ZZZZ', '5'))