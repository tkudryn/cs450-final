#!/usr/bin/python3
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import sys
import tkinter.ttk as ttk
import mysql.connector

#TODO: 
# Change buttons to reflect correct database
# Remove unncessary buttons
# Add correct views for correct actions (query, plot etc.)
# Add matplotlib code to create a plot using the results of the query
# Remove export query and export database
# Remove the insertion and removal pages
# Add plot page

'''
each class is a page in this set up
mainapp creates the initialization of the app's baseline
the for loop  holds a list that holds the names of all of the
other page classes to be passed into self.frames and loaded when their 
buttons are clicked.
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
            for F in (StartPage,QueryPage,InsertPage,QEPage,RemovePage,TEPage): #,PlotPage):
                frame = F(container,self)
                self.frames[F] = frame
                frame.grid(row=0,column=0,sticky="nsew")

            #Use controller.show_frame(Page'sClassName) on button command to load each page 
            self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

###########################
## EXPORT TABLE FUNCTION ##
###########################
        # Export bodytype
        def PROJECTE(self):
            # Open MySQL connection
            self.cnx = mysql.connector.connect(user='', password='', database='',host='')
            self.cur = self.cnx.cursor()
            self.command=("""SELECT * FROM project INTO OUTFILE '/home/username/ProjectExports/bodytype.csv';""")			
            self.cur.execute
            self.cur.execute(self.command)
            self.cnx.commit()
            self.cur.close()
            self.cnx.close()
		   

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

        insertbutton = tk.Button(self, text="Insert",command = lambda: controller.show_frame(InsertPage))                 
        insertbutton.pack()

        removebutton = tk.Button(self, text="Remove",command = lambda: controller.show_frame(RemovePage))
        removebutton.pack()

        # Suggest removing
        tableExbutton = tk.Button(self, text="Export Table",command = lambda: controller.show_frame(TEPage))
        tableExbutton.pack()

        # Suggest removing
        queryExbutton = tk.Button(self, text="Export Query",command = lambda: controller.show_frame(QEPage))
        queryExbutton.pack()
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
        self.cnx = mysql.connector.connect(user='', password='', database='',host='')
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


#############
#Insert Page#
#############
class InsertPage(tk.Frame):
    def INSERTION(self):
        # Assign text box stuff to variable
        self.make = self.make_entry.get() 
        self.model = self.model_entry.get()
        self.price = self.price_entry.get()
        self.platform = self.platform_entry.get()
        self.drive = self.drive_entry.get()
        self.aggrev = self.aggrev_entry.get()
        self.autonomous = self.autonomous_entry.get()
        #self.worth = self.worth_entry.get()
        #self.public = self.public_entry.get()
        self.critic = self.critic_entry.get()
        self.customer = self.customer_entry.get()
        self.construction = self.construction_entry.get()
        self.shape = self.shape_entry.get()
        self.suspension = self.suspension_entry.get()
        self.infotainment = self.infotainment_entry.get()
        self.proximity = self.proximity_entry.get()
        self.autobrake = self.autobrake_entry.get()
        self.adc = self.adc_entry.get()
        self.maintenance = self.main_entry.get()
        self.dep = self.dep_entry.get()
        self.recall = self.recalls_entry.get()

        # Output variables for testing
        print(self.make)
        print(self.model)
        print(self.price)
        print(self.platform)
        print(self.drive)
        print(self.aggrev) 
        print(self.autonomous)
        #print(self.worth)
        #print(self.public) 
        print(self.critic)
        print(self.customer) 
        print(self.construction)
        print(self.shape) 
        print(self.suspension) 
        print(self.infotainment) 
        print(self.proximity)
        print(self.autobrake) 
        print(self.adc)
        print(self.maintenance) 
        print(self.dep) 
        print(self.recall)

        # Assign vairables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='', password='', database='',host='')
        self.cur = self.cnx.cursor()

        # Body type query, has to go first due to Foreign key constraint
        self.query1 = ("""INSERT INTO body_type(platform_code, construction, shape, drive, suspension) VALUES(%s,%s,%s,%s,%s) """)
        self.data_value1 = (self.platform, self.construction, self.shape, self.drive, self.suspension)
        self.cur.execute(self.query1,self.data_value1)
        print("Body Type INSERTED")

        # Car query
        self.query2 = (""" INSERT INTO car(model,make,price,platform_code,drive,aggregate_review,autonomous) VALUES(%s,%s,%s,%s,%s,%s,%s)""")
        self.data_value2 = (self.model,self.make,self.price,self.platform,self.drive,self.aggrev,self.autonomous)
        self.cur.execute(self.query2,self.data_value2)
        print("Car INSERTED")

        # Review query
        self.query3 = ("""INSERT INTO review(model,critic_score,customer_score) VALUES(%s,%s,%s)""")
        self.data_value3 = (self.model,self.critic,self.customer)
        self.cur.execute(self.query3,self.data_value3)           
        print("Review INSERTED")

        # Tech query
        self.query4 = ("""INSERT INTO tech(model,infotainment,proximity_sensor,auto_braking,adc,autonomous) VALUES(%s,%s,%s,%s,%s,%s)""")
        self.data_value4 = (self.model,self.infotainment,self.proximity,self.autobrake,self.adc,self.autonomous)
        self.cur.execute(self.query4,self.data_value4)
        print("Tech INSERTED")

        # Cost of Ownership query
        self.query5 = ("""INSERT INTO costofownership(model,make,maintenance,depreciation,recalls) VALUES(%s,%s,%s,%s,%s)""")
        self.data_value5 = (self.model,self.make,self.maintenance,self.dep,self.recall)
        self.cur.execute(self.query5,self.data_value5)
        print("Cost of Ownership INSERTED")

        # Commit changes and close connection
        print("Insertion finished")
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
        print("Commited!")

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()

        label = tk.Label(self,text="Please fill out the form to insert a car into the database. No box may be left empty.")
        label.pack()

        ### Fields for Query ###

        ## Car Table ##
        # Make
        self.make_label = tk.Label(self, text = "Make: ")
        self.make_label.pack()
        self.make_entry = tk.Entry(self)
        self.make_entry.pack()

        # Model
        self.model_label = tk.Label(self, text = "Model: ")
        self.model_label.pack()
        self.model_entry = tk.Entry(self)
        self.model_entry.pack()

        # Price
        self.price_label = tk.Label(self, text = "Price: ")
        self.price_label.pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        # Platform Code
        self.platform_label = tk.Label(self, text = "Platform Code: ")
        self.platform_label.pack()
        self.platform_entry = tk.Entry(self)
        self.platform_entry.pack()

        # Drive
        self.drive_label = tk.Label(self, text = "Drive:")
        self.drive_label.pack()
        self.drive_entry = tk.Entry(self)
        self.drive_entry.pack()

        # Aggregate Review %
        self.aggrev_label = tk.Label(self, text = "Aggregate Review: (00.00)")
        self.aggrev_label.pack()
        self.aggrev_entry= tk.Entry(self)
        self.aggrev_entry.pack()

        # Autonomous
        self.autonomous_label = tk.Label(self, text = "Autonomous? (1/0)")
        self.autonomous_label.pack()
        self.autonomous_entry = tk.Entry(self)
        self.autonomous_entry.pack()

        ## Brand Table ##
        # Brand Worth
        #self.worth_label = tk.Label(self, text = "Worth: (00.00)")
        #self.worth_label.pack()
        #self.worth_entry = tk.Entry(self)
        #self.worth_entry.pack()
            
        # Public
        #self.public_label = tk.Label(self, text = "Public? (1/0)")
        #self.public_label.pack()
        #self.public_entry = tk.Entry(self)
        #self.public_entry.pack()

        ## Review Table ##
        # Critic Score
        self.critic_label = tk.Label(self, text = "Critic Score")
        self.critic_label.pack()
        self.critic_entry = tk.Entry(self)
        self.critic_entry.pack()

        # Customer Score
        self.customer_label = tk.Label(self, text = "Customer score")
        self.customer_label.pack()
        self.customer_entry = tk.Entry(self)
        self.customer_entry.pack()

        ## Body Type ##
        # Construction
        self.construction_label = tk.Label(self, text = "Construction")
        self.construction_label.pack()
        self.construction_entry = tk.Entry(self)
        self.construction_entry.pack()

        # Shape
        self.shape_label = tk.Label(self, text = "Shape")
        self.shape_label.pack()
        self.shape_entry = tk.Entry(self)
        self.shape_entry.pack()

        # Suspension
        self.suspension_label = tk.Label(self, text = "Suspension")
        self.suspension_label.pack()
        self.suspension_entry = tk.Entry(self)
        self.suspension_entry.pack()

        ## Tech ##
        # Infotainment Name
        self.infotainment_label = tk.Label(self, text = "Infotainment: (No spaces)")
        self.infotainment_label.pack()
        self.infotainment_entry = tk.Entry(self)
        self.infotainment_entry.pack()

        # Proximity Sensor
        self.proximity_label = tk.Label(self, text = "Proximity Sensor? (1/0)")
        self.proximity_label.pack()
        self.proximity_entry = tk.Entry(self)
        self.proximity_entry.pack()

        # Automatic Braking
        self.autobrake_label = tk.Label(self, text = "Automatic Braking? (1/0)")
        self.autobrake_label.pack()
        self.autobrake_entry = tk.Entry(self)
        self.autobrake_entry.pack()

        # Adaptive Cruise Control
        self.adc_label = tk.Label(self, text = "Adaptive Cruise? (1/0)")
        self.adc_label.pack()
        self.adc_entry = tk.Entry(self)
        self.adc_entry.pack()

        ## Cost of Ownership
        # Average Maintenance 
        self.main_label = tk.Label(self, text = "Average Maintenance: ")
        self.main_label.pack()
        self.main_entry = tk.Entry(self)
        self.main_entry.pack()

        # Annual Depreciation
        self.dep_lab = tk.Label(self, text = "Annual Depreciation: (00.00)")
        self.dep_lab.pack()
        self.dep_entry = tk.Entry(self)
        self.dep_entry.pack()

        # Recalls
        self.recalls_label = tk.Label(self, text = "Recalls: " )
        self.recalls_label.pack()
        self.recalls_entry = tk.Entry(self)
        self.recalls_entry.pack()

        # Back button
        backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor = "sw", side = "left")

        # Submit button
        submit = tk.Button(self, text='Insert',command=self.INSERTION)
        submit.pack(anchor = "sw", side = "right")


#############		
#Remove Page#
#############
class RemovePage(tk.Frame):
    def DELETE(self):
        print("Start")

        # Assign input to variable
        self.model = self.Entry1.get()
        self.platform = self.Entry2.get()

        # Print Variables for testing
        print(self.model)
        print(self.platform)

        # Create queries to remove items
        # Connect to MySQL database
        self.cnx = mysql.connector.connect(user='', password='', database='',host='')
        self.cur = self.cnx.cursor()

        # Create MySQL commands
        # REMOVAL ORDER tech -> cow -> review -> car -> body_type
        # Remove from Tech table
        #self.removal1 = ("""DELETE FROM tech WHERE model=%s""")
        self.removal1 = "DELETE FROM tech WHERE model=%s"
        #self.data_value1 = (self.model)
        self.cur.execute(self.removal1,(self.model,))
        print("Deleted from Tech table")

        # Remove from Cost of Ownership table
        self.removal2 = "DELETE FROM costofownership WHERE model=%s"
        self.cur.execute(self.removal2,(self.model,))
        print("Deleted from Cost of Ownership table")

        # Remove from Review table
        self.removal3 = "DELETE FROM review WHERE model=%s"
        self.cur.execute(self.removal3,(self.model,))
        print("Deleted from Review table")

        # Remove from car table
        self.removal4 = "DELETE FROM car WHERE model=%s"
        self.cur.execute(self.removal4,(self.model,))
        print("Deleted from Car table")

        # Remove from Body type table
        self.removal5 = "DELETE FROM body_type WHERE platform_code=%s"
        self.cur.execute(self.removal5,(self.model,))
        print("Deleted from Body Type table")

        # Commit changes and close connection
        print("Deletion finished")
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()
        print("Commited!")

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self,text="Please fill out the form below to remove a car from the database")
        label.pack()

        backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor = "sw", side = "left")

        #begin REMOVAL form code

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.1, rely=0.089, height=18, width=100)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Car Model''')

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.1, rely=0.311, height=18, width=150)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Platform Code''')

        ### SELECT FROM ###
        # Select input box
        self.Entry1 = tk.Entry(self)
        self.Entry1.place(relx=0.350, rely=0.089,height=20, relwidth=0.243)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        ###  WHERE STATEMENT ###
        # WHERE input box1
        self.Entry2 = tk.Entry(self)
        self.Entry2.place(relx=0.350, rely=0.311,height=20, relwidth=0.243)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        # Run Deletion Function Button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
        self.Button1.configure(text='''Remove Entry''')
        self.Button1["command"] = self.DELETE

###################		
#Export Query Page#
###################
class QEPage(tk.Frame):
    def EXPORT(self):
        # Assign vairables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='', password='', database='',host='')
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause
        if self.WHEREB == 0:
            self.query1 = ("SELECT {} FROM {} INTO OUTFILE '/home/username/ProjectExports/QueryExport.csv';".format(self.VALUE,self.TABLE))
            print(self.query1)
            self.cur.execute(self.query1)
            print("Simple Query")	

        # Create complicated query that uses WHERE clause
        if self.WHEREB == 1:
            self.query1 = ("SELECT {} FROM {} WHERE {} {} {} INTO OUTFILE '/home/username/ProjectExports/QueryExport.csv';".format(self.VALUE,self.TABLE,self.WHERE,self.WHEREV,self.WHERE2))
            #self.command=("""SELECT * FROM review INTO OUTFILE '/home/username/ProjectExports/DBoutput.csv';""")
            self.cur.execute(self.query1)


    def QUERY(self):
        print("Function Called")

        # Assign entry box values to variables
        self.VALUE = self.Entry1.get()
        self.TABLE = self.Entry2.get()
        self.WHERE = self.Entry3.get()
        self.WHERE2 = self.Entry4.get()
        self.WHEREB = self.CheckVar2.get()
        self.WHEREV = self.TCombobox1.get()

        # Output for testing, remove before submission
        print(self.VALUE) 
        print(self.TABLE)
        print(self.WHERE)
        print(self.WHERE2)
        print(self.WHEREB)
        print(self.WHEREV)
        #reset text to empty in case this is a subsequent call of QUERY
        self.Scrolledtext1.delete(1.0,"end")
        # Assign vairables to mysql statements and execute
        # Open MySQL connection
        self.cnx = mysql.connector.connect(user='', password='', database='',host='')
        self.cur = self.cnx.cursor()
        # Create simple query that doesn't use WHERE clause
        if self.WHEREB == 0:
            self.query1 = ("SELECT {} FROM {}".format(self.VALUE,self.TABLE))
            print(self.query1)
            self.cur.execute(self.query1)
            print("Simple Query")
            #loop that outputs query into text box
            for row in self.cur.fetchall():
                self.Scrolledtext1.insert("end", row)
                self.Scrolledtext1.update_idletasks()
                self.Scrolledtext1.insert("end", '\n')
                self.Scrolledtext1.update_idletasks()	

        # Create complicated query that uses WHERE clause
        if self.WHEREB == 1:
            self.query1 = ("SELECT {} FROM {} WHERE {} {} {}".format(self.VALUE,self.TABLE,self.WHERE,self.WHEREV,self.WHERE2))
            print(self.query1)
            self.cur.execute(self.query1)
            print("Complicated Query")
            #loop that outputs query into text box
            for row in self.cur.fetchall():
                self.Scrolledtext1.insert("end", row)
                self.Scrolledtext1.update_idletasks()
                self.Scrolledtext1.insert("end", '\n')
                self.Scrolledtext1.update_idletasks()


    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()

        label = tk.Label(self,text="Please fill out the form to query the database. No box may be left empty.")
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
        # Option checkbox for WHERE clause
        self.CheckVar2 = tk.IntVar()
        self.RadioWHERE = tk.Checkbutton(self, variable = self.CheckVar2, onvalue = 1, offvalue = 0)
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
        self.Scrolledtext1 = scrolledtext.ScrolledText(self)
        self.Scrolledtext1.place(relx=0.0, rely=0.667, relheight=0.262
        , relwidth=0.98)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(width=10)
        self.Scrolledtext1.configure(wrap="none")
        # Export button
        self.ExportQuery = tk.Button(self)
        self.ExportQuery.place(relx=0.35, rely=0.933, height=28, width=149)
        self.ExportQuery.configure(activebackground="#f9f9f9")
        self.ExportQuery.configure(text='''Export''')
        self.ExportQuery['command'] = self.EXPORT
        # Run Query button
        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.017, rely=0.578, height=28, width=92)
        self.Button1.configure(text='''Run Query''')
        self.Button1['command'] = self.QUERY


###################		
#Export Table Page#
###################
class TEPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        label = tk.Label(self,text="Please choose a table below to export")
        label.pack(anchor = "n",side = "top")

        backbutton = tk.Button(self, text="Back",command = lambda: controller.show_frame(StartPage))
        backbutton.pack(anchor = "sw", side = "left")
        Projecte = tk.Button(self, text="project",command = lambda: controller.PROJECTE())
        Projecte.pack()

app = mainapp()
app.mainloop()
