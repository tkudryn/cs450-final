import tkinter as tk
import StartPage
import StatisticsPage
import PlotPage
import Cloropleth
import Timeseries

class mainapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        # Don't forget to add new page classes to this list
        for F in (StartPage.StartPage, StatisticsPage.StatisticsPage, PlotPage.PlotPage, Cloropleth.Cloropleth, Timeseries.Timeseries):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Use controller.show_frame(Page'sClassName) on button command to load each page
        self.show_frame(StartPage.StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()