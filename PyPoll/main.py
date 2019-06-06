import os
import csv

csvpath = os.path.join('election_data.csv')

# Variables
total_votes = 0
candidate = 0
candidate_dict = {}


# Open CSV
with open(csvpath, 'r', newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(election_data)

    for row in election_data:
        candidate_name = row[2]

        if candidate_name in candidate_dict:
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1
        else:
            candidate_dict[candidate_name] = 1


        # calculate total votes
        # total_votes = total_votes + 1

    print(candidate_dict)



# # Summary Table
# print("Election Results")
# print("---------------------------")
# print(f"Total Votes: {total_votes}")
# print("---------------------------")
# # print(f"Khan Info")
# print(f"Correy Info")
# print(f"Li Info")
# print(f"O'Tooley Info")
# print("---------------------------")
# print(f"Winner: {winner name}")