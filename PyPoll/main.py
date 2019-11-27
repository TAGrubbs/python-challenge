import os
import csv

csvpath = os.path.join('..', 'Resources', 'PyPoll', 'election_data.csv')
poll = {}
totalVotes = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        totalVotes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
allCandidates = []
candidatesVotes = []

for key, value in poll.items():
    allCandidates.append(key)
    candidatesVotes.append(value)

percentOfVote = []
for n in candidatesVotes:
    percentOfVote.append(round(n/totalVotes*100, 1))

results = list(zip(allCandidates, candidatesVotes, percentOfVote))
winnerList = []

for name in results:
    if max(candidatesVotes) == name[1]:
        winnerList.append(name[0])

winner = winnerList[0]

if len(winnerList) > 1:
    for w in range(1, len(winnerList)):
        winner = winner + ", " + winnerList[w]

print("Election Results" + '\n')
print("-------------------------" + '\n')
print("Total Votes: " + str(totalVotes) + '\n')
print("-------------------------" + '\n')
for entry in results:
    print(entry[0] + ": " + str(entry[2]) +"%  (" + str(entry[1]) + ')\n')
print("-------------------------" + '\n')
print("Winner: " + str(winner))

file = open("Poll_Results.txt", "w") 
file.write("Election Results" + '\n')
file.write("-------------------------" + '\n')
file.write("Total Votes: " + str(totalVotes) + '\n')
file.write("-------------------------" + '\n')
for entry in results:
    file.write(entry[0] + ": " + str(entry[2]) +"%  (" + str(entry[1]) + ')\n')
file.write("-------------------------" + '\n')
file.write("Winner: " + str(winner))