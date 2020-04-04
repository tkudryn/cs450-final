import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import csv
import numpy as np

#used for line graph
DateCaseDict = {} #empty dictionary for storing dates and cases per date
deathsYvals = []
casesYvals = []
Xvals = []


#used for weekly barchat (chose not to append later)
incidence = [0,0,0,0,0,0,0,0,0,0,0,0]
mortality = [0,0,0,0,0,0,0,0,0,0,0,0]


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


            
#Deaths vs cases graph per date line graph
i=0
x=0
for key in DateCaseDict.keys():
    casesYvals.append(DateCaseDict[key][0])
    deathsYvals.append(DateCaseDict[key][1])
    Xvals.append(i)
    i = i + 1
    #print(row[0])

    
plt.plot(Xvals, casesYvals, c = 'b', label = "cases", linewidth = 3.0)
plt.plot(Xvals, deathsYvals, c = 'r', label = "deaths", linewidth = 3.0)
plt.xlim([0,70])
plt.ylim([0,190000])
plt.xlabel("days")
plt.ylabel("cases")
plt.title(label="Covid-19 cases. (Febuary - March)")
plt.legend()
plt.savefig("scaledCovid_linegraph.pdf")
#plt.show()
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
    
print(len(incidence))
print(incidence[2], incidence[3])
inds = np.arange(len(incidence))
plt.bar(inds, incidence, width=.85, color='blue', label='incidence')
plt.bar(inds, mortality, width=.85, color='red', label='mortality')
plt.legend(loc="upper left")
plt.title('Covid-19, weekly progression')
plt.xlabel('weeks')

#plt.xticks(inds + .45, weeks, rotation = 90)
#plt.show()
plt.savefig("weekly_barchart_covid.pdf")







