from tkinter import Tk


class Manager(Tk):
    def __init__(self):
        super().__init__()
        self.build()

    def build(self):
        self.title("Big Report - Main Menu")
        self.geometry("600x400")
        self.resizable(False, False)
