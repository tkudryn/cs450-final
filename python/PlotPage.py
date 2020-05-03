#Author: Emily Risley 
#Date: April 2020

import tkinter.ttk as ttk
import tkinter as tk
import Cloropleth
import Timeseries
import StartPage
import lab19
############
# PlotPage #
############
#navigation page for generating plots
class PlotPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self, text="Please select a plot type")
        label.pack()
		
		#navigation buttons
        querybutton = tk.Button(self, text="Cloropleth", command=lambda: controller.show_frame(Cloropleth.Cloropleth))
        querybutton.pack()

        querybutton = tk.Button(self, text="Time series", command=lambda: controller.show_frame(Timeseries.Timeseries))
        querybutton.pack()

        querybutton = tk.Button(self, text="Plot Report", command= lab19.plots)
        querybutton.pack()
		
        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage.StartPage))
        backbutton.pack(anchor="sw", side="left")
        # end buttons
	
