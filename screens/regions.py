from tkinter import Tk, Toplevel, Frame


class BigRegions(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.build()

    def build(self):
        self.title("Big Report - Regions")
        self.resizable(False, False)
