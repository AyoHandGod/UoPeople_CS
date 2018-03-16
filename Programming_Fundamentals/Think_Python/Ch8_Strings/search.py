def search(word, letter, pos):
    index = pos
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

print(search("taylor", 'r', 3))

in_both('carriers', 'sparriers')

print(is_reverse('stops', 'spots'))