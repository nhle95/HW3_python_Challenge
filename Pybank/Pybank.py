# import the OS module
import os

# import csv read module
import csv

#define csv path
csv_path='Resources/budget_data.csv'

#open csv path and skip header
with open(csv_path) as a:
	a = csv.reader(a, delimiter=",")
	header = next(a)
	
	#set variables
	pl_list = []
	average_monthlychange = []
	no_month_list = []
	
	#set initial value of the counter to zero
	sum_pl=0	
	monthcount=0
	sum_pl=0
	difference_pl=0
	previous_pl=0
	current_pl=0
	max_date=0
	min_date=0
	greatestincrease = 0
	worstdecrease = 0
	i=0
	
	for row in a: #need to stay within with open
		#print(row)
		monthcount+=1 #+= means it will add its current value to itself 
		sum_pl+= int(row[1])
		month=row[0]
		no_month_list.append(month)
		pl_list.append(row[1]) #add all column P&L to list
	totalmonth = len(no_month_list)
	#print(totalmonth)
	#print(sum_pl)
for i in range(totalmonth-1): #range from from first row to last row -1. because we want to later grab the current p&L (cannot count first data row since we dont have anything to subtract with) (prevent overflows)
	#print (i)
	current_pl = float(pl_list[i+1])
	previous_pl = float(pl_list [i])
	monthlychange= float(current_pl) - float(previous_pl)
	average_monthlychange.append(monthlychange)
	max_change = max(average_monthlychange)
	min_change = min(average_monthlychange)
	if monthlychange == max_change:
		max_date = i
	elif monthlychange == min_change:
		min_date = i

average_changeforperiod =round(sum(average_monthlychange) / (len(pl_list)-1),2)
	
analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {monthcount}\n\
Total : ${sum_pl}\n\
Average Change: ${average_changeforperiod}\n\
Greatest Increase in Profits: {no_month_list[max_date+1]} (${int(max_change)})\n\
Greatest Decrease in Profits: {no_month_list[min_date+1]} (${int(min_change)})\n'

#print to terminal
print(analysis)

#output text file

# create a new file
output_path = os.path.join("analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

       # Write analysis
    textfile.write(analysis)





		





