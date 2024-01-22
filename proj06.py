##############################################################################
#       Computer Project #6 
#       
#       function that reads a csv file for nba player stats
#           prompts for the proper file to open
#           give user for type of stat to receive
#           asks for user input on stat and player
#           displays the corresponding output for the stat and the player
#       reprompts for type of stat to receive, 'q' exits program
#
##############################################################################




##   NBAPlayerPlayoffData.csv



import csv
import operator

PLAYER ="Last_name, First_name,TEAM,POS,GP,MPG,Usage Rate,Turnover Rate,FTA,FT%,2PA,2P%,3PA,3P%,FG%,PointsPerGame,ReboundsPerGame,AssistsPerGame,StealsPerGame,BlocksPerGame,TurnoversPerGame,Offensive Rating"

def open_file():
    ''' Insert Docstring Here '''
    pass  # replace this line with code
    
    file_str = input("Input a file: ")
    
    while True:
        #is this part different, like don't open here?
        try:
            fp = open(file_str, "r") #this not needed?
            return fp
            
        except FileNotFoundError:
            print('Invalid filename, please try again.')
            file_str = input("Input a file: ")

def read_file(fp):
    ''' Insert Docstring Here '''
    #pass  # replace this line with code
    
    reader = csv.reader(fp)
    next(reader,None) #skips header
    
    master_list = []
    
    for line in reader:
        
        master_list.append(line)
    
    #print(master_list)
    return sorted(master_list)
    

def process_file(master_list):
    ''' Insert Docstring Here '''
    #pass  # replace this line with code
    
    newmaster_list = []
    
    for line in master_list:
        
        fullname = line[0].split()
        
        newlist = [fullname[1],fullname[0],line[1],line[2]]
        
    
            
        value = line[3:]
        for i in value:
            
            try:
                value_flt = float(i)
            
                newlist.append(value_flt)
                
            except ValueError:
                value_flt = float(0.0)
                
                newlist.append(value_flt)
            
            
        newmaster_list.append(newlist)
    
    return sorted(newmaster_list)
            
        

def get_team_list(master_list):
    ''' Insert Docstring Here '''
    #pass  # replace this line with code
    
    

def get_players_on_team (master_list,team):
    ''' Insert Docstring Here '''
    #pass  # replace this line with code
    # initialize team list to []
    team_list = []
    
    # loop through each player in my master list
    #for line in newmaster_list:
        
    #   get player's last name, first name, team
    
    
    #   if player's team = team parameter:
    #       create a player string in the specified format
    #       append player to team list
    # return team list(remember to sort)
    # (remember to handle case of team parameter being invalid)
    # return None    

def get_top_ten (master_list,stat):
    ''' Insert Docstring Here '''
    pass  # replace this line with code

def get_bottom_ten (master_list,stat):
    ''' Insert Docstring Here '''
    pass  # replace this line with code

def get_players_in_position (master_list,position):
    ''' Insert Docstring Here '''
    pass  # replace this line with code

def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Top 10 players for a statistic 
    2: Bottom 10 players for a statistic
    3: Get players for a position 
    4: Get players on a team
    5: Get list of teams\n"""
    print(OPTIONS)


def main():
    #pass # replace this line with code
    
    fp = open_file()
    master_list = read_file(fp)
    process_file(master_list)
    option_str = input('Choose an option, q to quit: ')
    
    #loops until input of 'q' occurs 
    while option_str != 'q':
        
        #error checking to validate correct input of user
        while not (option_str=='1' or option_str=='2' or option_str=='3' \
        or option_str=='4' or option_str=='5' or option_str=='q'):
            print("Error: incorrect option, please try again.")
            option_str = input('Choose an option, q to quit: ')

#from proj05            
##############Change this loop to what we need            
        
        # if option_str == '1':
        #     master_list, stat = get_top_ten()
        #     
        #     statop_str = input("Enter the statistic: ")
        #     
        #     
        #     
        #     option_str = input("Select and option, q to quit: ")
        
        # #used for age 12 and older vac value    
        # elif option_str =='2':
        #     min_val, min_county, max_val, max_county = \
        #     find_min_max_column(fp, 136, 154)
        #     s = "age 12 and older"
        #     display_min_max(s,min_val, min_county, max_val, max_county)
        #     display_options()
        #     option_str = input("Select and option, q to quit: ")
        
        # #used for age 18 and older vac value
        # elif option_str == '3':
        #     min_val, min_county, max_val, max_county = \
        #     find_min_max_column(fp, 183, 201)
        #     s = "age 18 and older"
        #     display_min_max(s,min_val, min_county, max_val, max_county)
        #     display_options()
        #     option_str = input("Select and option, q to quit: ")
        
        # #used for age 65 and older vac value
        # elif option_str == '4':
        #     min_val, min_county, max_val, max_county = \
        #     find_min_max_column(fp, 230, 234)
        #     s = "age 65 and older"
        #     display_min_max(s,min_val, min_county, max_val, max_county)
        #     display_options()
        #     option_str = input("Select and option, q to quit: ")
        
        # #ends program
        # elif option_str == 'q':
        #     break
        
        # #gives value for total vac value in michigan
        # elif option_str == '5':
        #     allvac_int = all_vaccinated(fp)
        #     print("\nTotal vaccinated in Michigan: {:,d}".format(allvac_int))
        #     display_options()
        #     option_str = input("Select and option, q to quit: ")

########################################change this loop to what we need    

if __name__ == '__main__':
    main()