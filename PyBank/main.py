import os
import csv
import numpy as np
csvpath = os.path.join('..', 'Resources', 'Pybank', 'budget_data.csv')

dates= []
profitOrLoss= []
totalPOL= []
netvalue= 0
months=0 
averageChange=0
roundedAverageChange= 0
isFirstRow = True
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        months += 1
        dates.append(row[0])
        profitOrLoss.append(int(row[1]))
        if isFirstRow:
            netvalue = int(row[1])
            isFirstRow = False
        else:
            netvalue = int(row[1]) - netvalue
            totalPOL.append(int(netvalue))
        netvalue=int(row[1])


minIndx = np.argmin(totalPOL)
maxIndx = np.argmax(totalPOL)
averageChange = (sum(totalPOL)/len(totalPOL))
roundedAverageChange= (round(averageChange, 2))
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(sum(profitOrLoss)))
print("Average  Change: $" + str(roundedAverageChange))
print("Greatest Increase in Profits: " + str(dates[maxIndx+1]) + " (" + str(profitOrLoss[(maxIndx+1)]) + ")")
print("Greatest Decrease in Profits: " + str(dates[(minIndx+1)]) + " (" + str(profitOrLoss[(minIndx+1)]) + ")")

file = open("Bank_Results.txt", "w") 
file.write("Financial Analysis"+ '\n')
file.write("----------------------------"+ '\n')
file.write("Total Months: " + str(months)+ '\n')
file.write("Total: $" + str(sum(profitOrLoss))+ '\n')
file.write("Average  Change: $" + str(roundedAverageChange)+ '\n')
file.write("Greatest Increase in Profits: " + str(dates[maxIndx+1]) + " (" + str(profitOrLoss[(maxIndx+1)]) + ")"+ '\n')
file.write("Greatest Decrease in Profits: " + str(dates[(minIndx+1)]) + " (" + str(profitOrLoss[(minIndx+1)]) + ")"+ '\n')
file.close() 