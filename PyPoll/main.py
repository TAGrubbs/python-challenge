import os
import csv

# Identifies file with poll data
csvpath = os.path.join('..', 'Resources', 'PyPoll', 'election_data.csv')
poll = {}
total_votes = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
allcandidates = []
candidates_votes = []

for key, value in poll.items():
    allcandidates.append(key)
    candidates_votes.append(value)

percentofvote = []
for n in candidates_votes:
    percentofvote.append(round(n/total_votes*100, 1))

results = list(zip(allcandidates, candidates_votes, percentofvote))
winner_list = []

for name in results:
    if max(candidates_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

print("Election Results" + '\n')
print("-------------------------" + '\n')
print("Total Votes: " + str(total_votes) + '\n')
print("-------------------------" + '\n')
for entry in results:
    print(entry[0] + ": " + str(entry[2]) +"%  (" + str(entry[1]) + ')\n')
print("-------------------------" + '\n')
print("Winner: " + str(winner))

file = open("results.txt", "w") 
file.write("Election Results" + '\n')
file.write("-------------------------" + '\n')
file.write("Total Votes: " + str(total_votes) + '\n')
file.write("-------------------------" + '\n')
for entry in results:
    file.write(entry[0] + ": " + str(entry[2]) +"%  (" + str(entry[1]) + ')\n')
file.write("-------------------------" + '\n')
file.write("Winner: " + str(winner))