from tkinter import Tk, Menu


class Manager(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.menu()

    def build(self):
        self.title("Big Report - Main Menu")
        self.geometry("600x400")
        self.resizable(False, False)

    def menu(self):
        self.menuBar = Menu()

        self.optionTables = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Tables", menu=self.optionTables)

        self.optionTables.add_command(label="Regions")
        self.optionTables.add_command(label="Countries")
        self.optionTables.add_command(label="LCs")
        self.optionTables.add_separator()
        self.optionTables.add_command(label="Franchises")
        self.optionTables.add_separator()
        self.optionTables.add_command(label="Exit", command=self.quit)

        self.optionData = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Data", menu=self.optionData)

        self.optionData.add_command(label="Main")
        self.optionData.add_command(label="Marketing")
        self.optionData.add_separator()
        self.optionData.add_command(label="Exchange Rates")

        self.optionViews = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Views", menu=self.optionViews)

        self.optionReports = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Reports", menu=self.optionReports)

        self.optionSetup = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="SetUp", menu=self.optionSetup)

        self.optionAbout = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="About", menu=self.optionAbout)

        self.config(menu=self.menuBar)
