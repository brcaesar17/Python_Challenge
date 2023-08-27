import os # import the os library to dynamically access the csv file over various operating systems 
import csv # import csv library to access and external csv file 

# Construct the path to the CSV file using os.path.join
file_path = os.path.join("Resources", "budget_data.csv")
Exp_Pybank = os.path.join ("analysis", "Results_PyBank.txt")

# variable to store list of profit / losses
Profit = [] # list to store profit / olossess values 

deviation = [] # the diffirence between profit/ losses month by month

dates = []# list to store months / dates of the profit/loss values 


# initial value of counter
count = 0

# variable to store total profit / losses
TotalValue = 0

#variable to store  change in profit / losses
greatest = 0
decrease = 0

total_changes = 0
# Print the constructed file path
print(file_path)

# Open and read the CSV file
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

 # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    # At this point, csv_reader is a generator that iterates through the rows of the CSV file
    # You can iterate through the rows using a loop
    for row in csv_reader:
        TotalValue = TotalValue + int(row[1])
        Profit.append (int(row[1]))
        dates.append(row[0])
        count += 1
        
    print('Financial Analysis')
    print('...........................')
    print('the total number of Months is', count)
    print('Total value of the profit / loss is',TotalValue)
    #average will be outside for loop and it will be sum of profit divided over len of prof/loss
    #print('Total Months',len(Profit[row])-1)
for i in range(len(Profit) - 1):
    dif = int(Profit[i+1]) - int(Profit[i]) # the diffirence in profit/loss between a month and susequnt one 
    deviation.append(dif)# assign the diffirence to a new list 
    if dif > greatest:
        greatest = dif # calculate the maximum diffirence or change in value 
    if dif < decrease:
        decrease = dif # calculate the minimum diffirence or change in value 
    total_changes += dif# calculate the total changes for changes month by month
average_change = total_changes / (len(Profit)-1) #  calulate the average of changes 

date_max = dates[deviation.index(max(deviation))+1]# assign the month of maximum change by using index method to the variable date_max
date_min = dates[deviation.index(min(deviation))+1]# assign the month of minimum change by using index method to the variable date_min
#print("The average change is:", average_change)
#print(f"The greatest increase is: {date_max} ({greatest}) ")
#print(f"The greatest decrease is: {date_min} ({decrease}) ")
results = f'''results
.....................
{("The greatest increase is:", greatest)}
{("The greatest decrease is:", decrease)}
{("The average change is:", average_change)}
{("The greatest increase is:", date_max, greatest)}
{("The greatest decrease is:", date_min, decrease)}
...............................'''
print(results)
with open(Exp_Pybank,'w') as txtfile:  
     txtfile.write(results)
#print("The greatest increase is:", greatest)
#print("The greatest decrease is:", decrease)



