#Author: Emily Risley 
#Date: April 2020

import tkinter as tk
import sys
import tkinter.ttk as ttk
import mysql.connector
import credentials
import PlotPage
import StartPage
import PlotCloropleth

#generates cloropleth page with fields for  date (form YYYY-MM-DD), 
# type (cases, deaths, rate of death)
#runs database query
#prints and saves generated choropleth
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
        
        if self.TYPE == '(deaths/cases) AS rate':
            self.TYPE = 'rate'
        PlotCloropleth.PlotCloropleth(self.cur.fetchall(), self.TYPE, self.DATE)
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
        backbutton = tk.Button(self, text="Back", command=lambda: controller.show_frame(PlotPage.PlotPage))
        backbutton.pack(anchor="sw", side="left")

        homebutton = tk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage.StartPage))
        homebutton.pack(anchor="sw", side="right")
        
		# begin Query form code

		#Date Label
        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.183, rely=0.089, height=28, width=50)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Date''')

		#Type Label
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