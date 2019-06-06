import os
import csv

csvpath = os.path.join('budget_data.csv')

total_months = 0
net_total = 0
last_month_revenue = 0
revenue_change = 0
revenue_change_list = []
total_changes = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
row_of_greatest_increase = [] # [date, income, change]
row_of_greatest_decrease = [] # [date, income, change]


with open(csvpath, 'r', newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    csv_header = next(budget_data)
    for row in budget_data:

        current_revenue = int(row[1])
        row.append(current_revenue - last_month_revenue)
        last_month_revenue = current_revenue

        # creates list of revenue changes
        revenue_change_list.append(row[2])

        # Finds greatest increase and decrease
        if not row_of_greatest_decrease:
            row_of_greatest_decrease = row
        elif row_of_greatest_decrease[2] > row[2]:
            row_of_greatest_decrease = row

        if not row_of_greatest_increase:
            row_of_greatest_increase = row
        elif row_of_greatest_increase[2] < row[2]:
            row_of_greatest_increase = row

        # calculate total months
        total_months = total_months + 1

        # calculates net total 
        net_total = net_total + current_revenue


# Calculates Average Change
total_changes = (sum(revenue_change_list[1:86])) # skips 0 to leave out first number in list
average_change = total_changes / 85 # there is probably a better way
average_change = round(average_change, 2)


print(row_of_greatest_increase)
# summary table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {row_of_greatest_increase[0]} (${row_of_greatest_increase[2]})")
print(f"Greatest Decrease in Profits: {row_of_greatest_decrease[0]} (${row_of_greatest_decrease[2]})")

# exports result to text file
write_file = f"financial_analysis.txt"
filewriter = open(write_file, mode = 'w')

filewriter.write("Financial Analysis\n")
filewriter.write("----------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Total: ${net_total}\n")
filewriter.write(f"Average  Change: ${average_change}\n")
filewriter.write(f"Greatest Increase in Profits: {row_of_greatest_increase[0]} (${row_of_greatest_increase[2]})\n")
filewriter.write(f"Greatest Decrease in Profits: {row_of_greatest_decrease[0]} (${row_of_greatest_decrease[2]})\n")

filewriter.close()