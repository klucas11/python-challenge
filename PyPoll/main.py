import os
import csv

# Variables
csvpath = os.path.join('election_data.csv')

total_votes = 0
candidate_dict = {}
winner_name = ""

# function to find candidates vote percentage
def calculate_percent_of_votes(total_votes, candidate):
    value = candidate / total_votes
    percent_of_votes = value * 100
    return round(percent_of_votes,2)

# Open CSV
with open(csvpath, 'r', newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")


    csv_header = next(election_data) # skips header

    for row in election_data:

        # Creates dictionary {"Name": Votes}
        candidate_name = row[2]

        if candidate_name in candidate_dict:
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1
        else: 
            candidate_dict[candidate_name] = 1

        # calculate total votes
        total_votes = total_votes + 1

# # Summary Table
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")

max_value = 0
for candidate in candidate_dict:
    print(f"{candidate}: {calculate_percent_of_votes(total_votes, candidate_dict[candidate])}% ({candidate_dict[candidate]})")
    
    if candidate_dict[candidate] > max_value:
        max_value = candidate_dict[candidate]
        winner_name = candidate

print("---------------------------")
print(f"Winner: {winner_name}")
print("---------------------------")
