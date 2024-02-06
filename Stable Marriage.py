



#Pseudocode
     
     #Create an empty list for possible engagements
     #Create an empty list for single men

     #Create a function to initialize a list of free men
        #function init__free_men():
                  #For each man in men_preference_list:
                    #Add man to free_men list

     ## Create a Function to perform the stable matching
        #function stable_matching():
                  # While free_men is not empty:
                     #For each man in free_men:
                        #Began to match them by calling begin_matching function()
      
      #Create a function to began the matching  for a man
           #function begin_matching():
                      #for a women in men_preference list 
                         #check if the women is  engaged or not
                            #if women is single :
                                 #the man can be engaged to the women ,so append there names to the possible_engagement list
                            #else if the women is not single:
                                 #check the index of her present pathner,in the woman_preference_list
                                  #check the index of the potential partner (man) in the woman's preference list
                                            #If the present_partner has lower index than the potential_patner(man):
                                                  #do nothing (pass)as the women is satisfied with her present_pathner
                                            #Else:
                                                   #The potential pathner(new man) is now engaged to the woman
                                                   #Remove the new man (potential_pathner)  the free_man list
                                                   #Append the present_man(the previously engaged man) to the free_man list
                                                   #Update the new man to be the present_pathner of the women
        
      #Create a main function
           #Call init_free_men() function
           #Call stable_matchinh() function
                
              # Open the output.txt file in and direct the output to the file output.txt in write mode as output_file
              # For each couple in possible_engagements:
                #Write each couple's name to output file in a new line everytime
        #If __name__ is "__main__":
            
              #Open input.txt in read mode as file
              # Read and execute the list of preferences from input.txt file


       # Call the main function to perform stable matching and generate output
    
   

import os


# keeps record of possible engagements
possible_engagements = []

# keeps record of men who are single and need to be engaged
free_men = []

def _init_free_men():
    #initializes the list of single men with all available men
    for man in men_preference_list.keys():
        free_men.append(man)

def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            #start the matching process for each man in the list
            begin_matching({'man': man})

def begin_matching(args):
    man = args['man']
    for woman in men_preference_list[man]:
        # checks for matches where the woman's status is taken or engaged
        matches = [couple for couple in possible_engagements if woman in couple]

        if len(matches) == 0:
            # if the woman is free, the man proposes to her and they get engaged
            possible_engagements.append([man, woman])
            free_men.remove(man)
            break
        elif len(matches) != 0:
            # if the woman is taken, then her preferences are compared 
            present_partner = women_preference_list[woman].index(matches[0][0])
            potential_partner = women_preference_list[woman].index(man)

            if present_partner < potential_partner:
                pass  # the woman is satisfied with her present partner so no further action is required
            else:
                # the new man aka the potential partner is now engaged to the woman
                free_men.remove(man)

                # the previous man aka the present partner is single and free now 
                free_men.append(matches[0][0])

                # the previous man is updated to be the new man up for a match
                matches[0][0] = man
                break

def main():
    _init_free_men()
    stable_matching()

    # open the output.txt file (in write mode) and direct the output to the file
    with open('output.txt', 'w') as output_file:
        for couple in possible_engagements:
            output_file.write(f'{couple[0]} {couple[1]}\n')

if __name__ == "__main__":
    # read and execute the list of preferences from input.txt file
    with open('input.txt', 'r') as file:
        exec(file.read())

    main()

# changes the working directory to its original location if needed
# original_directory = "C:/Users/arsha/OneDrive/Desktop/assignment1"
# os.chdir(original_directory)
