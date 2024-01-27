import sys
   

def remove_garbage(log_file):
    ''' for removing garbage value'''
    try:
        with open(log_file,"r+") as file:
            lines = file.readlines()
        
            
            correct_list = [] # to store the correct data
            for line in lines:
                    line = line.strip()
                    data = line.split(',')

                    try:
                        which_cat = data[0].strip()
                        arriving_time = data[1].strip()
                        departing_time = data[2].strip()           # catching exceptions
                    
                        arriving_time = int(arriving_time) 
                        departing_time = int(departing_time)
                        difference = departing_time - arriving_time
                    except:
                        continue
                   
                    
                    
                    if which_cat == "THEIRS" and difference == 1:
                        correct_list.append(line)
                    elif which_cat == "OURS" and difference > 0:
                        correct_list.append(line)
                                
            return correct_list
                    # file.seek(0)
                    # file.writelines(correct_list)
                    # file.truncate()
    except FileNotFoundError:
        print(f'Cannot open "{log_file}"!')             
                          
                            
# main processing code    
               
def cat_shelter(correct_list):
    try:
                with open("test1.log","w") as file:
                     file.write('\n'.join(correct_list))
                   
                with open("test1.log", 'rt') as file:
                   lines = file.readlines()
                    
            

                # declaring variables
                our_cat_visits = 0
                their_cat_visits = 0
                total_stay = 0
                longest_visit = 0
                shortest_visit = float('inf')

                
                for line in lines:
                    data = line.strip().split(',')

            
                    which_cat = data[0]
                    arriving_time = data[1]
                    departing_time = data[2]

                    arriving_time = int(arriving_time) 
                    departing_time = int(departing_time)

                    visit_duration = departing_time - arriving_time

                    # for OURS
                    if which_cat == "OURS":
                        our_cat_visits += 1
                        total_stay += visit_duration
                        longest_visit = max(longest_visit, visit_duration)
                        shortest_visit = min(shortest_visit, visit_duration)
                        
                    # for THEIRS
                    elif which_cat == "THEIRS":
                        their_cat_visits += 1
                        
                # time in hours and minutes
                total_hours = total_stay // 60
                total_minutes = total_stay % 60
                avg_time = total_stay // max(1, our_cat_visits) #incase the our cat visits is 0.
                

                
                print("Log File Analysis")
                print("==================\n")
                print(f"Cat Visits: {our_cat_visits}")
                print(f"other Cats: {their_cat_visits}\n")
                print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
                if avg_time < 60:
                    print(f"Average Visit Length: {avg_time} Minutes")
                elif avg_time >= 60:
                    print(f"Average Visit Length: {avg_time//60} hours , {avg_time % 60} minutes")
                print(f"Longest Visit: {longest_visit} Minutes")
                print(f"Shortest Visit: {shortest_visit} Minutes")
       

    except FileNotFoundError:
       print(f'Cannot open "test1.log"!')
            
#  to check if command-line argument is present
if len(sys.argv) > 2:
    print("Can only send one file at a time!")
elif len(sys.argv) < 2:
    print("Missing command line argument!")
else:
    # Analyze the cat shelter log file
    correct_file = remove_garbage(sys.argv[1])
    if correct_file:
        cat_shelter(correct_file)




