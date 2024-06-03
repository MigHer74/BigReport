from tkinter import Toplevel, LabelFrame, Frame, Label, Entry


class BigRegions(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.build()

    def build(self):
        self.title("Big Report - Regions")
        self.resizable(False, False)

        self.regionsFrame = Frame(self)
        self.regionsFrame.pack()

        self.headerFrame = LabelFrame(self.regionsFrame)
        self.headerFrame.grid(row=0, column=0)

        self.idLabel = Label(self.headerFrame, text="Id:")
        self.idLabel.grid(row=0, column=0)

        self.idEntry = Entry(self.headerFrame, width=5)
        self.idEntry.grid(row=0, column=1)

        self.nameLabel = Label(self.headerFrame, text="Name:")
        self.nameLabel.grid(row=0, column=2)

        self.nameEntry = Entry(self.headerFrame, width=25)
        self.nameEntry.grid(row=0, column=3)
