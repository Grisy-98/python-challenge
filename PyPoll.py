import os
import csv

#Get csv file
csvpath = os.path.join( "Resources", "election_data.csv")
#Create txt file to write the results
f = open("PyPoll_Results.txt", "w")
print("Election Results", file=f)
print("---------------------------------------------", file=f)

#Get total number of votes
rowcount = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter="," )
    csv_header = next(csvreader)
    for row in csvreader:
        rowcount += 1
    print(f"Total Votes: {rowcount}", file=f)
print("---------------------------------------------", file=f)

#Complete list of all canidates who recieved votes
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
#Get the names of the candidates
# print(unique(candidates))

#Count the number of votes each candidate got
charles_count = candidates.count("Charles Casper Stockham")
diana_count = candidates.count("Diana DeGette")
raymon_count = candidates.count("Raymon Anthony Doane")

#Calculate the percentage of votes
charles_percent = round(((charles_count / len(candidates))*100), 3)
diana_percent = round(((diana_count / len(candidates))*100), 3)
raymon_percent = round(((raymon_count / len(candidates))*100), 3)

#Print the results with the candidate name, percentage of votes, and vote totals
print(f"Charles Casper Stockham: {charles_percent}% ({charles_count})", file=f)
print(f"Diana DeGette: {diana_percent}% ({diana_count})", file=f)
print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_count})", file=f)
print("---------------------------------------------", file=f)

#Announce the winning candidate
if (charles_count > diana_count) and (charles_count > raymon_count):
    print("Winner: Charles Casper Stockham", file=f)
elif (diana_count > charles_count) and (diana_count > raymon_count):
    print("Winner: Diana DeGette", file=f)
elif (raymon_count > diana_count) and (raymon_count > charles_count):
    print("Winner: Raymon Anthony Doane", file=f)

f.close()