#!/usr/bin/python3
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import sys
import tkinter.ttk as ttk
import mysql.connector
import credentials

# TODO:
# Add matplotlib code to create a plot using the results of the query
# Add plot page

'''
Overview of application
'''


class mainapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        # Don't forget to add new page classes to this list
        for F in (StartPage, StatisticsPage, PlotPage, Cloropleth, Timeseries):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Use controller.show_frame(Page'sClassName) on button command to load each page
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


############
# Start Page#
############
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

        querybutton = tk.Button(self, text="Statistics", command=lambda: controller.show_frame(StatisticsPage))
        querybutton.pack()

        plotExButton = tk.Button(self, text="Create Plot", command=lambda: controller.show_frame(PlotPage))
        plotExButton.pack()
        # end buttons


###########
# StatisticsPage#
###########
class StatisticsPage(tk.Frame):
    def STATS(self):
        print("Function Called")

        # Assign entry box values to variables
        self.STATE = self.Entry1.get()
        self.DATE = self.Entry2.get()
        self.TYPE = self.Entry3Choice.get()

        #COLUMN is what goes in select statement
        self.COLUMN = self.TYPE

        # Output for testing, remove before submission
        print(self.STATE)
        print(self.TYPE)

        #create syntax for rate column
        if self.TYPE == 'rate of death':
            self.COLUMN = '(deaths/cases)'
            self.TYPE = 'rate'

        # create syntax for state conditional (if all states, do not specify)
        if self.STATE == "All":
            self.STATE = ''

            #syntax for SUM is different for rate than cases or deaths
            if (self.TYPE == 'rate'):
                self.COLUMN = 'SUM(deaths)/SUM(cases)'
            else:
                self.COLUMN = 'SUM(' + self.COLUMN + ')'
        else:
            self.STATE = "AND state = '" + self.STATE + "'"

        # reset text to empty in case this is a subsequent call of QUERY
        self.Scrolledtext2.delete(1.0, "end")
        # Assign variables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='project', password=credentials.password, database='cs450', host=credentials.host)
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause

        # need to figure out how to do "all" for state
        self.query1 = (
            "SELECT {} FROM {} WHERE date = '{}' {}".format(self.COLUMN, "project", self.DATE, self.STATE, self.TYPE))
        print(self.query1)
        self.cur.execute(self.query1)
        print("Simple Query")
        # loop that outputs query into text box

        self.Scrolledtext2.insert("end", self.cur.fetchall()[0])
        self.Scrolledtext2.update_idletasks()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self, text="Please fill out the form below to Query the database")
        label.pack()

        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor="sw", side="left")
        # begin Query form code

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.183, rely=0.089, height=28, width=46)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''State''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.183, rely=0.2, height=28, width=46)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Date''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.183, rely=0.311, height=18, width=46)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Type''')

        # Select input box
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.4, rely=0.089, height=20, relwidth=0.4)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        # Select input box
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.4, rely=0.2, height=20, relwidth=0.4)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        # type input box
        self.Entry3Choice = tk.StringVar()
        self.Entry3Choice.set("cases")  # default value
        self.Entry3 = tk.OptionMenu(self, self.Entry3Choice, "cases", "deaths", "rate of death")
        self.Entry3.place(relx=0.4, rely=0.311, height=30, relwidth=0.4)

        # Query OutPut box
        self.Scrolledtext2 = scrolledtext.ScrolledText(self)
        self.Scrolledtext2.place(relx=0.0, rely=0.667, relheight=0.262
                                 , relwidth=0.98)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(font="TkTextFont")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="#c4c4c4")
        self.Scrolledtext2.configure(width=10)
        self.Scrolledtext2.configure(wrap="none")
        # Run Query button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
        self.Button1.configure(text='''Run Query''')
        self.Button1["command"] = self.STATS


############
# PlotPage #
############
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
        querybutton = tk.Button(self, text="Cloropleth", command=lambda: controller.show_frame(Cloropleth))
        querybutton.pack()

        querybutton = tk.Button(self, text="Time series", command=lambda: controller.show_frame(Timeseries))
        querybutton.pack()

        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor="sw", side="left")
        # end buttons


class Timeseries(tk.Frame):
    def PLOT(self):
        print("Function Called")

        # Assign entry box values to variables
        self.STATE = self.Entry1.get()
        self.TYPE = self.Entry2Choice.get()

        # Output for testing, remove before submission
        print(self.STATE)
        print(self.TYPE)

        # Assign variables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='project', password=credentials.password, database='cs450', host=credentials.host)
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause

        #create syntax for rate column
        if self.TYPE == 'rate of death':
            self.TYPE = '(deaths/cases) AS rate'

        # create syntax for state conditional (if all states, do not specify)
        if self.STATE == "All":
            self.STATE = ''
        else:
            self.STATE = "WHERE state = '" + self.STATE + "'"

        self.query1 = ("SELECT state, date, {} FROM {} {} ".format(self.TYPE, "project", self.STATE))
        print(self.query1)
        self.cur.execute(self.query1)
        print("Plot")
        print(self.cur.fetchall())
        # send to plot function self.cur.fetchall(), self.PLOTTYPE
        #call python fun (self.cur.fetchall(), self.PLOTTYPE)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self, text="Please fill out the form below to generate the plot")
        label.pack()

        # Navigation Buttons
        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor="sw", side="left")

        homebutton = tk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        homebutton.pack(anchor="sw", side="right")
        # begin Query form code

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.183, rely=0.089, height=28, width=50)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''State''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.183, rely=0.2, height=18, width=50)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Type''')

        # State input box
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.4, rely=0.089, height=20, relwidth=0.4)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        # type input box
        self.Entry2Choice = tk.StringVar()
        self.Entry2Choice.set("cases")  # default value
        self.Entry2 = tk.OptionMenu(self, self.Entry2Choice, "cases", "deaths", "rate of death")
        self.Entry2.place(relx=0.4, rely=0.2, height=30, relwidth=0.4)

        # Run Query button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
        self.Button1.configure(text='''PLOT''')
        self.Button1["command"] = self.PLOT

class Cloropleth(tk.Frame):
    def PLOT(self):
        print("Function Called")

        # Assign entry box values to variables
        self.DATE = self.Entry1.get()
        self.TYPE = self.Entry2Choice.get()

        # Output for testing, remove before submission
        print(self.DATE)
        print(self.TYPE)

        # Assign variables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='project', password=credentials.password, database='cs450', host=credentials.host)
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause

        #create syntax for rate column
        if self.TYPE == 'rate of death':
            self.TYPE = '(deaths/cases) AS rate'

        self.query1 = ("SELECT state, {} FROM {} where date='{}' ".format(self.TYPE, "project", self.DATE))
        print(self.query1)
        self.cur.execute(self.query1)
        print("Plot")
        print(self.cur.fetchall())
        # send to plot function self.cur.fetchall()


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self, text="Please fill out the form below to generate the plot")
        label.pack()

        # Navigation Buttons
        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(PlotPage))
        backbutton.pack(anchor="sw", side="left")

        homebutton = tk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        homebutton.pack(anchor="sw", side="right")
        # begin Query form code

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.183, rely=0.089, height=28, width=50)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Date''')


        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.183, rely=0.2, height=18, width=50)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Plot type''')

        # State input box
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.4, rely=0.089, height=20, relwidth=0.4)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        # type input box
        self.Entry2Choice = tk.StringVar()
        self.Entry2Choice.set("cases")  # default value
        self.Entry2 = tk.OptionMenu(self, self.Entry2Choice, "cases", "deaths", "rate of death")
        self.Entry2.place(relx=0.4, rely=0.2, height=30, relwidth=0.4)

        # Run Query button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
        self.Button1.configure(text='''PLOT''')
        self.Button1["command"] = self.PLOT
app = mainapp()
app.minsize(300, 300)
app.mainloop()
