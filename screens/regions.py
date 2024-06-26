from tkinter import ttk, Toplevel, LabelFrame, Frame, Label, Entry, Button


class BigRegions(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.focus()
        self.build()

    def build(self):
        self.title("Big Report - Regions")
        self.resizable(False, False)

        self.regionsFrame = Frame(self)
        self.regionsFrame.pack()

        self.headerFrame = LabelFrame(self.regionsFrame)
        self.headerFrame.grid(row=0, column=0, padx=10, pady=10)

        self.idLabel = Label(self.headerFrame, text="Id:")
        self.idLabel.grid(row=0, column=0, padx=(10, 5), pady=10)

        self.idEntry = Entry(self.headerFrame, width=5)
        self.idEntry.grid(row=0, column=1, padx=(0, 10), pady=10)

        self.nameLabel = Label(self.headerFrame, text="Name:")
        self.nameLabel.grid(row=0, column=2, padx=(10, 5), pady=10)

        self.nameEntry = Entry(self.headerFrame, width=25)
        self.nameEntry.grid(row=0, column=3, padx=(0, 10), pady=10)

        self.treeFrame = LabelFrame(self.regionsFrame)
        self.treeFrame.grid(row=1, column=0, padx=10, pady=10)

        self.treeRegions = ttk.Treeview(self.treeFrame, columns=(1, 2),
                                        show="headings", height=15,
                                        selectmode="browse")

        self.treeRegions.heading(1, text="Id")
        self.treeRegions.heading(2, text="Region Name")

        self.treeRegions.column(1, width=75, anchor="center")
        self.treeRegions.column(2, width=200)

        self.treeRegions.grid(row=0, column=0, padx=10, pady=10)

        self.buttonsFrame = Frame(self.regionsFrame)
        self.buttonsFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

        self.buttonSave = Button(self.buttonsFrame, text="Save", width=10)
        self.buttonSave.grid(row=0, column=0, pady=10)

        self.buttonDelete = Button(self.buttonsFrame, text="Delete", width=10)
        self.buttonDelete.grid(row=1, column=0)

        self.buttonClose = Button(self.buttonsFrame, text="Close", width=10,
                                  command=self.destroy)
        self.buttonClose.grid(row=2, column=0, pady=(20, 0))
