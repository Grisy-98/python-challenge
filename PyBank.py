import os
import csv

#Get csv file
csvpath = os.path.join( "Resources", "budget_data.csv")

#Create txt file to write the results
f = open("PyBank_Results.txt", "w") 
print("Financial Analysis", file=f )
print("---------------------------------------------", file=f)

#The total number of months included in the dataset
rowcount = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter="," )
    csv_header = next(csvreader)
    for row in csvreader:
        rowcount += 1
    print(f"Total Months: {rowcount}", file=f)

#Set each column as a list
filename = open('Resources/budget_data.csv','r')
file = csv.DictReader(filename)

date = []
profit_loss = []
for col in file:
    date.append(col['Date'])
    profit_loss.append(col['Profit/Losses'])
#The net total amount of "Profit/Losses" over the entire period
profit_loss = list(map(int, profit_loss))
total = sum(profit_loss)
print(f"Total: ${total}", file=f)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
total_diff = 0
for i in range(1, len(profit_loss)):
    total_diff += profit_loss[i] - profit_loss[i-1]

avg_diff = round(total_diff / (len(profit_loss)-1), 2)
print(f"Average Change: ${avg_diff}", file=f)

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
change = []
for i in range(1, len(profit_loss)): 
    change.append(profit_loss[i]-profit_loss[i-1])
max_val = max(change)
max_ind = change.index(max_val)+1
print(f"Greatest Increase in Profits: {date[max_ind]} (${max_val})", file=f)
min_value = min(change)
min_ind = change.index(min_value)+1
print(f"Greatest Decrease in Profits: {date[min_ind]} (${min_value})", file=f)

f.close()

