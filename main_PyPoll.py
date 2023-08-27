import os # import library to dynamically access the file location on various operating systems
import csv # import library to read external csv file
election_data = os.path.join('Resources', 'election_data.csv')
analysis_export = os.path.join("analysis", "results.txt")
overall = 0 # variable to store overall number of csv file rows ( overall number of votes)
candidates_list = [] # list to store list of candidates list (three candidates)
votes_list = [] # list to store list number of votes
with open (election_data, encoding='UTF-8' ) as file: # open the csv file in order read it row by row
    election_reader = csv.reader(file, delimiter =',') # read the file taking into condideration the ',' will distinguish between the column and the dubsequent one
    election_header = next(election_reader) # read the header of the file , and skip it in case not available
    for row in election_reader: # looping the election file in order to answer the questions
        overall += 1 # counter to show how many votes overall for all candidates
        if row[2] not in candidates_list:# if the name of the candidate not exist within the candidate list add it
            candidates_list.append(row[2]) # add the candidate name into the list
            index = candidates_list.index(row[2]) # index is a variable to store the first row number of each candidate occured
            votes_list.append(1)  # add the number one to each row of list votes
        else:
             index = candidates_list.index(row[2])
             votes_list[index]+=1
# gather results in f-string
results = f'''Election Results
-------------------------------------------------------
Total Votes: {overall}
-------------------------------------------------------
{candidates_list[0]}: {(votes_list[0]/overall)*100:.3f}% ({votes_list[0]})
{candidates_list[1]}: {(votes_list[1]/overall)*100:.3f}% ({votes_list[1]})
{candidates_list[2]}: {(votes_list[2]/overall)*100:.3f}% ({votes_list[2]})
-------------------------------------------------------
Winner: {candidates_list[votes_list.index(max(votes_list))]}
-------------------------------------------------------'''
# print results
print(results)
# export txt file of results
with open(analysis_export,'w') as txtfile:                             # open new file
    txtfile.write(results)
   
 
   

   
        
   

      
                       
             
             
            
            



        