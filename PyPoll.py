import os
import csv

#Get csv file
csvpath = os.path.join( "Resources", "election_data.csv")

print("Election Results")
print("---------------------------------------------")

#Get total number of votes
rowcount = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter="," )
    csv_header = next(csvreader)
    for row in csvreader:
        rowcount += 1
    print(f"Total Votes: {rowcount}")
print("---------------------------------------------")

#Complete list of canidates who recieved votes, percentage of votes, and amount of votes

filename = open('Resources/election_data.csv','r')
file = csv.DictReader(filename)

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)

candidates = []
for col in file:
    candidates.append(col['Candidate'])
print(unique(candidates))