from tkinter import ttk, Toplevel, LabelFrame, Frame, Label, Entry, Button


class BigCountries(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.focus()
        self.build()

    def build(self):
        self.title("Big Report - Countries")
        self.resizable(False, False)

        self.countriesFrame = Frame(self)
        self.countriesFrame.pack()

        self.headerFrame = LabelFrame(self.countriesFrame)
        self.headerFrame.grid(row=0, column=0, padx=10, pady=10)

        self.idLabel = Label(self.headerFrame, text="Id:")
        self.idLabel.grid(row=0, column=0, padx=(10, 5), pady=10)

        self.idEntry = Entry(self.headerFrame, width=5)
        self.idEntry.grid(row=0, column=1, padx=(0, 10), pady=10)

        self.nameLabel = Label(self.headerFrame, text="Country:")
        self.nameLabel.grid(row=0, column=2, padx=(10, 5), pady=10)

        self.nameEntry = Entry(self.headerFrame, width=25)
        self.nameEntry.grid(row=0, column=3, padx=(0, 10), pady=10)

        self.regionLabel = Label(self.headerFrame, text="Region:")
        self.regionLabel.grid(row=0, column=4, padx=(10, 5), pady=10)

        self.regionCombobox = ttk.Combobox(self.headerFrame,
                                           width=5,
                                           values=["NA", "CA", "SA"],
                                           state="readonly")
        self.regionCombobox.grid(row=0, column=5, padx=(0, 10), pady=10)

        self.treeFrame = LabelFrame(self.countriesFrame)
        self.treeFrame.grid(row=1, column=0, padx=10, pady=10)

        self.treecountries = ttk.Treeview(self.treeFrame, columns=(1, 2, 3),
                                          show="headings",
                                          height=15, selectmode="browse")

        self.treecountries.heading(1, text="Id")
        self.treecountries.heading(2, text="Country Name")
        self.treecountries.heading(3, text="Region")

        self.treecountries.column(1, width=80, anchor="center")
        self.treecountries.column(2, width=250)
        self.treecountries.column(3, width=80, anchor="center")

        self.treecountries.grid(row=0, column=0, padx=10, pady=10)

        self.buttonsFrame = Frame(self.countriesFrame)
        self.buttonsFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

        self.buttonSave = Button(self.buttonsFrame, text="Save", width=10)
        self.buttonSave.grid(row=0, column=0, pady=10)

        self.buttonDelete = Button(self.buttonsFrame, text="Delete", width=10)
        self.buttonDelete.grid(row=1, column=0)

        self.buttonClose = Button(self.buttonsFrame, text="Close", width=10,
                                  command=self.destroy)
        self.buttonClose.grid(row=2, column=0, pady=(20, 0))
