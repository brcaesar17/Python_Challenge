import csv # import library to read external csv file 
import os # import library to dynamically access the file location on various operating systems

overall = 0 # variable counter to store overall number of csv file rows ( overall number of votes)

candidates_list = [] #  to store names of candidates  (three candidates)

percent_vote = []

votes_number = [] # list to store the number of votes for each candidate



election_data = os.path.join('Resources', 'election_data.csv')
# define the csv file path and access its location 
#election_data = 'Resources/election_data.csv'

with open (election_data, encoding='UTF-8' ) as file: # open the csv file in order read it row by row
    
    election_reader = csv.reader(file, delimiter =',') # read the file taking into condideration the ',' will distinguish between the column and the dubsequent one

    election_header = next(election_reader) # read the header of the file , and skip it in case not available

    for row in election_reader: # looping the election file in order to answer the questions
        overall += 1 # counter to show how many votes overall for all candidates 

        if row[2] not in candidates_list:# if the name of the candidate not exist within the candidate list add it 
            candidates_list.append(row[2]) # add the candidate name into the list      
            options = candidates_list.index(row[2]) # options is a variable to store the first occurr of candidate name
            votes_number.append(1)  # add the number one to each row of list to count votes of each candidate       
        else:
            options = candidates_list.index(row[2])# assign the locatoin of each candidate name in the list to variable options
            votes_number[options] += 1 # counter will give us the total number of votes for each candidate
    
    

    print(' Election Results:')       
    print('......................')

    print(' total votes:', overall )
    print('......................')

    #print(votes_number)
    #print('......................')
                   
    for i in votes_number: # looping the votes_number list which contains total numbers of each candidates to calculate the percentage and define the winner
        percentage = (i/overall) 
        #percentage = round(percentage)
        percentage = f"{percentage:.2%}"
        percent_vote.append(percentage)# list to store the percentages of each candidate votes 
        winner = max(votes_number)# maximum number of votes 
        index = votes_number.index(winner)
        winning_candidate = candidates_list[index]
  
    #print('winner votes number',winner)
    #print('percentage of voting ',percent_vote)
    for i in range (len(candidates_list)):
        print(f"{candidates_list[i]}:{str(percent_vote[i])}: {str(votes_number[i])}")
        print('.........................................')
    print ('winning candidate: ', winning_candidate)

   
        
   

      
                       
             
             
            
            



        