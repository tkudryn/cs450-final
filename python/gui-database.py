#!/usr/bin/python3
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import sys
import tkinter.ttk as ttk
import mysql.connector

#TODO: 
# Add matplotlib code to create a plot using the results of the query
# Add plot page

'''
Overview of application
'''

class mainapp(tk.Tk):
	
        def __init__(self, *args, **kwargs ):
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)

            container.pack(side="top",fill="both",expand=True )

            container.grid_rowconfigure(0,weight=1)
            container.grid_rowconfigure(0,weight=1)

            self.frames = {}
            #Don't forget to add new page classes to this list
            for F in (StartPage,QueryPage): #,PlotPage):
                frame = F(container,self)
                self.frames[F] = frame
                frame.grid(row=0,column=0,sticky="nsew")

            #Use controller.show_frame(Page'sClassName) on button command to load each page 
            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

############
#Start Page#
############
#Start Page is the first page you see in the application
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self,text="Start page")
        label.pack()

        #begin buttons
        quitbutton = tk.Button(self, text="QUIT",command = lambda: controller.quit())
        quitbutton.pack(anchor = "nw", side = "left")

        querybutton = tk.Button(self, text="Query",command = lambda: controller.show_frame(QueryPage))
        querybutton.pack()

        plotExButton = tk.Button(self, text="Create Plot",command = lambda: controller.show_frame(PlotPage))
        plotExButton.pack()
        #end buttons


###########
#QueryPage#
###########
class QueryPage(tk.Frame):
    def QUERY(self):
        print("Function Called")

        # Assign entry box values to variables
        self.VALUE = self.Entry1.get()
        self.TABLE = self.Entry2.get()
        self.WHERE = self.Entry3.get()
        self.WHERE2 = self.Entry4.get()
        self.WHEREB = self.CheckVar1.get()
        self.WHEREV = self.TCombobox1.get()

        # Output for testing, remove before submission
        print(self.VALUE)
        print(self.TABLE)
        print(self.WHERE)
        print(self.WHEREB)
        print(self.WHEREV)
        #reset text to empty in case this is a subsequent call of QUERY
        self.Scrolledtext2.delete(1.0,"end")
        # Assign vairables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='project', password='', database='cs450',host='')
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause
        if self.WHEREB == 0:
            self.query1 = ("SELECT {} FROM {}".format(self.VALUE,self.TABLE))
            print(self.query1)
            self.cur.execute(self.query1)
            print("Simple Query")
            #loop that outputs query into text box
            for row in self.cur.fetchall():
                self.Scrolledtext2.insert("end", row)
                self.Scrolledtext2.update_idletasks()
                self.Scrolledtext2.insert("end", '\n')
                self.Scrolledtext2.update_idletasks()	

        # Create complicated query that uses WHERE clause
        if self.WHEREB == 1:
            self.query1 = ("SELECT {} FROM {} WHERE {} {} {}".format(self.VALUE,self.TABLE,self.WHERE,self.WHEREV,self.WHERE2))
            print(self.query1)
            self.cur.execute(self.query1)
            print("Complicated Query")
            #loop that outputs query into text box
            for row in self.cur.fetchall():
                self.Scrolledtext2.insert("end", row)
                self.Scrolledtext2.update_idletasks()
                self.Scrolledtext2.insert("end", '\n')
                self.Scrolledtext2.update_idletasks()


    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self,text="Please fill out the form below to Query the database")
        label.pack()

        backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor = "sw", side = "left")
        #begin Query form code

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.183, rely=0.089, height=28, width=46)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''SELECT''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.183, rely=0.2, height=18, width=46)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''FROM''')

        self.Label3 = tk.Label(self)
        self.Label3.place(relx=0.183, rely=0.311, height=18, width=46)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''WHERE''')

        # Select input box
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.317, rely=0.089,height=20, relwidth=0.243)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        # FROM input box
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.317, rely=0.2,height=20, relwidth=0.243)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")
        #WHERE STATEMENT
        # WHERE input box1
        self.Entry3 = tk.Entry(self)
        self.Entry3.place(relx=0.317, rely=0.311,height=20, relwidth=0.243)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")
        # WHERE Input box2
        self.Entry4 = tk.Entry(self)
        self.Entry4.place(relx=0.633, rely=0.311,height=20, relwidth=0.243)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        # Check Box for WHERE
        #self.RadioWHERE = tk.Radiobutton(self)
        self.CheckVar1 = tk.IntVar()
        self.RadioWHERE = tk.Checkbutton(self,variable = self.CheckVar1, onvalue = 1, offvalue = 0)
        self.RadioWHERE.place(relx=0.017, rely=0.302, relheight=0.044
        , relwidth=0.145)
        self.RadioWHERE.configure(activebackground="#f9f9f9")
        self.RadioWHERE.configure(justify='left')
        self.RadioWHERE.configure(text='''WHERE?''')
        # Drop down menu for WHERE statement logicals
        self.TCombobox1 = ttk.Combobox(self)
        self.TCombobox1.place(relx=0.567, rely=0.311, relheight=0.04
        , relwidth=0.062)
        self.value_list = ['AND','OR','>','<','=','!=']
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(takefocus="")
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
        self.Button1["command"] = self.QUERY

############
# PlotPage #
############

# Repurpose code from the Query page as much as possible

app = mainapp()
app.mainloop()
