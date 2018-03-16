def right_justify(word):
    wLen = len(word)
    spaces = 70 - wLen
    print(" " * spaces + word)

right_justify('Dante')
