fin = open('words.txt', 'r')

def large_words(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

large_words('words.txt')

def has_no_e(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        for letter in word