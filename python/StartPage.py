import tkinter as tk
import tkinter.ttk as ttk
import StatisticsPage
import PlotPage
# Start Page is the first page you see in the application
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self, text="Start page")
        label.pack()

        # begin buttons
        quitbutton = tk.Button(self, text="QUIT", command=lambda: controller.quit())
        quitbutton.pack(anchor="nw", side="left")

        querybutton = tk.Button(self, text="Statistics", command=lambda: controller.show_frame(StatisticsPage.StatisticsPage))
        querybutton.pack()

        plotExButton = tk.Button(self, text="Create Plot", command=lambda: controller.show_frame(PlotPage.PlotPage))
        plotExButton.pack()
        # end buttons
