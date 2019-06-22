import os
import csv
csvpath = os.path.join('..', 'Resources', 'Pybank', 'budget_data.csv')

dates= []
pORl= []
totalPOL= []
netvalue= 0
months=0 
AvgChange=0
RAvgChange= 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        months += 1

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        dates.append(row[0])
        pORl.append(int(row[1]))

isFirstRow = True
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if isFirstRow:
            netvalue = int(row[1])
            isFirstRow = False
        else:
            netvalue = int(row[1]) - netvalue
            totalPOL.append(int(netvalue))
        netvalue=int(row[1])

#zipdLists = zip(dates, pORl, totalPOL)
#dictstocks = dict(zipdLists)

#print(sum(totalPOL)/len(totalPOL))
#print(months)
import numpy as np

minIndx = np.argmin(totalPOL)
#print(dates[(minIndx+1)])
maxIndx = np.argmax(totalPOL)
#print(dates[(maxIndx+1)])
AvgChange = (sum(totalPOL)/len(totalPOL))
RAvgChange= (round(AvgChange, 2))
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(sum(pORl)))
print("Average  Change: $" + str(RAvgChange))
print("Greatest Increase in Profits: " + str(dates[maxIndx+1]) + " (" + str(pORl[(maxIndx+1)]) + ")")
print("Greatest Decrease in Profits: " + str(dates[(minIndx+1)]) + " (" + str(pORl[(minIndx+1)]) + ")")

file = open("results.txt", "w") 
file.write("Financial Analysis"+ '\n')
file.write("----------------------------"+ '\n')
file.write("Total Months: " + str(months)+ '\n')
file.write("Total: $" + str(sum(pORl))+ '\n')
file.write("Average  Change: $" + str(RAvgChange)+ '\n')
file.write("Greatest Increase in Profits: " + str(dates[maxIndx+1]) + " (" + str(pORl[(maxIndx+1)]) + ")"+ '\n')
file.write("Greatest Decrease in Profits: " + str(dates[(minIndx+1)]) + " (" + str(pORl[(minIndx+1)]) + ")"+ '\n')
file.close() 