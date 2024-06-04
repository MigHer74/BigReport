from tkinter import ttk, Toplevel, LabelFrame, Frame, Label, Entry, Button


class BigCountries(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.focus()
        self.build()

    def build(self):
        self.title("Big Report - Contries")
        self.resizable(False, False)
