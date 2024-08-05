PyBank Challenge:

In this challenge, I made sure to import os and csv in order to be able to import the needed csv files, read the csv files, and write the txt file of the results at the end.
For this specific challenge, I created two lists, one called "date" and the other called "profit_loss", in order to be able to import the information of each column. The reason for this was to make it easier to count the total number of months as well as calculate the total profits/losses, the average change, the greatest increase, and the greatest decrease. Additionally, demonstrating when the greatest increase and the greatest decrease occurred. 
To find the total number of months, I counted the amount of rows, excluding the header, that were given on the csv file.
To find the total profit/loss, I found the sum of the "Profit/Loss" column by changing the data type of the list, "profit_loss", become an integer and then used the sum function.
To find the average change, I created a variable called "total_diff" to calculate the total difference of the column. In order to find the total difference, a for-loop was created. Once the total difference was calculated, we needed to find the average by taking that ammount and dividing it by the total number of enteries in the "Profit/Loss" column. I also rounded the average to the nearest hundredth. 
Lastly, the greatest increase and greatest decrease in profit needed to be found. What I first did was create an empty list called "change" so it can hold the values of the difference from one row to the next. Then, I created a for-loop so it can run through all the data to find the difference and fill in the list. Using the "change" list, I found both, the maximum value and the minimum value. Using these values, I then found the corresponding date to show when the greatest increase and decrease in profits occurred. 

---------------------------------------------------------------------------------------------------------------------

PyPoll Challenge

In this challenge, I made sure to import os and csv in order to be able to import the needed csv files, read the csv files, and write the txt file of the results at the end.
Specifically for this challenge, I only created one list from the given inforamtion called "candidates". To populate this list, I ran a for-loop that read each row in the column "Candidate".
After that, I created a function called "unique" that will take a given list and create a new list with the unique values of the given list. I created this function in order to be able to see all the different candidates that were found in this csv file.
Once I knew how many different candidates there were and who are they, I then used the count function to see how many votes did each candidate receive.
Next, I calculated the percentage by dividing the number of votes each candidate received by the total number of votes, and then multiplying the quotient by 100. I also rounded the result to the nearest thousandths. 
Then, I printed the candidate's name along with the percentage of votes and the total number of votes that they each received.
Lastly, I used if and if-else statements to print the winning candidate.
