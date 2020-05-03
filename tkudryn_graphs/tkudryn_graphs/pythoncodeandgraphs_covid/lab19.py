import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import csv
import numpy as np

# all the graphs are placed into one big function to making calling this program much easier
def plots():
    #used for line graph
    DateCaseDict = {} #empty dictionary for storing dates and cases per date
    deathsYvals = []
    casesYvals = []
    Xvals = []
    #predefined variables 
    wsDeaths = 0
    msDeaths = 0
    esDeaths = 0
    ddDeaths = 0

    wsCases = 0
    msCases = 0
    esCases = 0
    ddCases = 0

    #Creating three lists to sort the states into four categories.
    #Western, Mid, eastern and the detached states (hawaii/alaska).
    detachedStates = ["Alaska", "Hawaii"]

    westernStates = ["Washington", "Oregon", "California", "Arizona", "Idaho", "Utah", "Nevada"]

    midStates = ["Montana", "Wyoming", "Colorado", "New Mexico", "Texas", "Oklahoma", "Kansas",
                 "Nebraska","South Dakota", "North Dakota","Minnesota","Iowa", "Missouri",
                 "Arkansas", "Lousiana", "Mississippi", "Tenesse","Alabama", "Kentucky","Illionios",
                 "Wisconsin", "Michigan", "Indiana", "Ohio","West Virginia"]

    easternStates = ["Florida", "Georgia", "South Carolina", "North Calorina", "Virginia",
                     "District of Columbia", "Maryland", "Delaware", "Pennsylvania", "New York",
                     "Delaware", "New Jersey", "Connecticut", "Rhode Island", "Massachussets",
                     "New Hampshire", "Vermont", "Maine"]

    #wil define these later to use them in a piechart
    totalDeaths = 0
    totalCases = 0


    #used for weekly barchat (chose not to append later)
    incidence = [0,0,0,0,0,0,0,0,0,0,0,0]
    mortality = [0,0,0,0,0,0,0,0,0,0,0,0]

    #importing file
    states = open("us-states.csv", "r")
    statesDict = csv.DictReader(states)
    keys = ['date', 'state', 'fips', 'cases', 'deaths']
    
    for row in statesDict:
       

        dateKey = row['date']
        cases = int(row['cases'])
        deaths = int(row['deaths'])
        
            
        if dateKey not in DateCaseDict:
            DateCaseDict[dateKey] = []
            DateCaseDict[dateKey].append(cases)
            DateCaseDict[dateKey].append(deaths)
        else:
            DateCaseDict[dateKey][0] = DateCaseDict[dateKey][0] + cases
            DateCaseDict[dateKey][1] = DateCaseDict[dateKey][1] + deaths

        #finding out case and death counts per region
        if row['state'] in detachedStates:
            ddCases += cases
            ddDeaths += deaths
            
        elif row['state'] in westernStates:
            wsCases += cases
            wsDeaths = deaths
            continue
            
        elif row['state'] in midStates:
            msCases += cases
            msDeaths += deaths

        else:
            esCases += cases
            esDeaths += deaths

                
    #Deaths vs cases graph per date line graph
    i=0
    x=0
    for key in DateCaseDict.keys():
        casesYvals.append(DateCaseDict[key][0])
        deathsYvals.append(DateCaseDict[key][1])
        Xvals.append(i)
        i = i + 1
        
    ylimiter = casesYvals[len(casesYvals)-1]

    
    plt.plot(Xvals, casesYvals, c = 'b', label = "cases", linewidth = 3.0)
    plt.plot(Xvals, deathsYvals, c = 'r', label = "deaths", linewidth = 3.0)
    plt.xlim([0,len(Xvals)-1])
    plt.ylim([0,ylimiter])
    plt.xlabel("days")
    plt.ylabel("cases")
    plt.title(label="Covid-19 cases")
    plt.legend()
    plt.savefig("Covid_linegraph.pdf")
    plt.show()
    plt.close()


    #log scaled bar chart below to see a more detailed look of the graph
    #bare in mind that the scaling is will heavely scew thw data to make it look
    #there are alot more deaths. If an overview of how many deats occured in comparison
    #to total cases Please look at the piechart or the non scaled line graph
    plt.yscale('log')
    plt.plot(Xvals, casesYvals, c = 'b', label = "cases", linewidth = 3.0)
    plt.plot(Xvals, deathsYvals, c = 'r', label = "deaths", linewidth = 3.0)
    plt.xlim([0,len(Xvals)-1])
    plt.ylim([0,ylimiter])
    plt.xlabel("days")
    plt.ylabel("cases")
    plt.title(label="Log Scaled Covid-19 cases")
    plt.legend()
    plt.savefig("Covid_linegraph_logscaled.pdf")
    plt.show()
    plt.close()


        
        
    #barchart plotting below
    i=0
    x=0

    for j in range(0,len(casesYvals)):
        incidence[x] = incidence[x] + casesYvals[j] #creating x and y vals for bar chart
        mortality[x] = mortality[x] + deathsYvals[j]
        if i == 6:
           i = 0
           x += 1
        i+=1
        
    inds = np.arange(len(incidence))
    plt.bar(inds, incidence, width=.85, color='blue', label='incidence')
    plt.bar(inds, mortality, width=.85, color='red', label='mortality')
    plt.legend(loc="upper left")
    plt.title('Covid-19, weekly progression')
    plt.xlabel('weeks')
    plt.show()
    plt.savefig("weekly_barchart_covid.pdf")
    plt.clf() #clearing plot


    #Preprocessing data for a pie chart bellow for Cases vs Deaths
    for i in deathsYvals:
        totalDeaths += i

    for i in casesYvals:
        totalCases += i
        

    labels = ["cases", "deaths"]
    pieChartVals = [totalCases, totalDeaths]
    #used for making a section of the pie chart sticks out
    explode = [0, 0.225]
    #customizable colors
    colors = ["gray","r"]


    plt.pie(pieChartVals, labels = labels, autopct="%.01f%%", explode = explode, colors = colors)
    plt.savefig("pieCharts_covid_representation.pdf")
    plt.show()
    plt.clf()



    #pieChart for percentagges of cases per region
    labels = ["Western cases","Detached","Mid","Eastern"]

    pieChartVals = [wsCases, ddCases, msCases, esCases]
    plt.title("Regional Covid 19 case ratios")
    plt.pie(pieChartVals, labels = labels)
    plt.savefig("regional_Covid_19_pieChart_cases.pdf")
    plt.show()
    plt.clf()


    pieChartVals = [wsDeaths, ddDeaths, msDeaths, esDeaths]
    plt.title("Regional Covid 19 death ratios")
    plt.pie(pieChartVals, labels = labels)
    plt.savefig("regional_Covid_19_pieChart_deaths.pdf")
    plt.show()
    plt.clf()

plots()

