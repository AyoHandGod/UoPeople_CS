from tkinter import messagebox
from random import randint

result = messagebox.showinfo("Some window Label", "Goodbye, World!")

class Puzzle:
    def __init__(self):
        self.items = {}
        self.position = None


    def main_frame(self):
        d = self.items
        print('+-----' * 4 + '+')
        print('|{0}|{1}|{2}|{4}|')