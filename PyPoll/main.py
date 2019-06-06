import os
import csv

csvpath = os.path.join('election_data.csv')

# Variables
total_votes = 0
candidate = 0
candidate_list = []
candidate0_votes = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate_vote_list = []

# Open CSV
with open(csvpath, 'r', newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(election_data)

    for row in election_data:
        
        # Creates list of candidates
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        # Calculate each candidates votes
        if row[2] == candidate_list[0]:
            candidate0_votes = candidate0_votes + 1
        elif row[2] == candidate_list[1]:
            candidate1_votes = candidate1_votes + 1       
        elif row[2] == candidate_list[2]:
            candidate2_votes = candidate2_votes + 1
        else:
            candidate3_votes = candidate3_votes + 1

        # calculate total votes
        total_votes = total_votes + 1

    # Adds each candidates votes to list
    candidate_vote_list.append(candidate0_votes)
    candidate_vote_list.append(candidate1_votes)
    candidate_vote_list.append(candidate2_votes)
    candidate_vote_list.append(candidate3_votes)



print(candidate_list)
print(candidate_vote_list)
# Summary Table
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
# print(f"Khan Info")
# print(f"Correy Info")
# print(f"Li Info")
# print(f"O'Tooley Info")
# print("---------------------------")
# print(f"Winner: {winner name}")