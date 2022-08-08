# import the OS module
import os

# import csv read module
import csv

#define csv path
csv_path='Resources/election_data.csv'

#open csv path and skip header
with open(csv_path) as a:
	a = csv.reader(a, delimiter=",")
	header = next(a)

#define variables
	voters_list = []
	candidate_list= []
	unique_name_list = []
	percent_list = []
	unique_vote_list = []
	no_vote = 0
	
	for row in a:
		#count the total number of votes
		no_vote+=1
		voters=row[0]
		#voters_list.append(voters)
		#totalrow = int(len(voters_list))
		#store all candidates names in list
		candidate_list.append(row[2])
		#create a set from candidate list to remove duplicate candidate names
	for i in set(candidate_list):
		unique_name_list.append(i)
		#counteach is the total of votes each unique candidates received
		counteach = candidate_list.count(i)
		unique_vote_list.append(counteach)
		#percent is the percentage of votes each unique candidates received
		percent = (counteach/no_vote)*100
		format_percent = round(percent,3) #format percentage to 3 decimals
		percent_list.append(format_percent)

win_vote = max(unique_vote_list) #find out who received the most vote
winner = unique_name_list[unique_vote_list.index(win_vote)] #find out who is the winner

print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(no_vote))    
print("-------------------------")
for i in range(len(unique_name_list)):
            print(unique_name_list[i] + ": " + str(percent_list[i]) +"% (" + str(unique_vote_list[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")





# create a new file
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as textfile:
	textfile.write(f"Election Results\n")
	textfile.write(f"------------------------------------\n")
	textfile.write(f"Total Votes : {no_vote}\n")
	textfile.write(f"------------------------------------\n")
	for i in range(len(unique_name_list)):
		textfile.write(f"{unique_name_list[i]} : {percent_list[i]}% ({unique_vote_list[i]})\n")
	textfile.write(f"------------------------------------\n")
	textfile.write(f"The winner is:  {winner}\n")
	textfile.write(f"------------------------------------\n")
