##############################################################################
#   Computer Project #5
#       function that reads from another file and outputs wanted info
#           takes in input from user on what data is wanted from vac info
#           uses the prompted input to give associate with file info
#       displays info on determined by the prompt           
#       prompt user again to continue to find different info
#       ends program with input of 'q'
#
##############################################################################


def reset_file_pointer_to_beginning(fp):
    """
    DO NOT CHANGE
    Resets file pointer to the beginning and returns updated file pointer
    
    Parameters: file pointer object
    return: file pointer object
    """
    fp.seek(0)
    return fp

def open_file():
    ''' 
    Asks the user to input a file to use, if not correct, reprompts user for 
    valid file input until correct
    
    Parameters: None
    return: file_pointer
    displays: prompt and error message as appropriate
    '''
    
    
    file_str = input('Input a file for reading: ')
    while True:
        try:
            fp = open(file_str, "r")
            return fp
            
        except FileNotFoundError:
            print('Invalid filename, please try again.')
            file_str = input('Input a file for reading: ')
            
#this one gets called, assume s is correct?        
def fix_county_string(s):
    ''' 
    Takes in a string s and makes sure it ends in county then returns it,
    if it does not it will append the appropriate letters to the end of s
    
    Paramters:str
    returns:str
    displays: nothing
    '''
    
    #depending on end of string, adds the approriate letters
    if s[-1] == 'y':
        return s
    
    elif s[-1] == 't':
        
        s += 'y'
        return s
    
    elif s[-1] == 'n':
        
        s += 'ty'
        return s
    
    elif s[-1] == 'u':
        
        s += 'nty'
        return s
    
    elif s[-1] == 'o':
        
        s += 'unty'
        return s
    
    elif s[-1] == 'C':
        
        s += 'ounty'
        return s
    
    else:
        return s
    
            
    

def find_min_max_column(fp,start,end):
    ''' 
    This function starts by calling and resetting the file to the beginning,
    and also skips over the first line(header). It then loops for each line
    in the file, grabs the index associeted with the vaccine data, then
    returns the min/max values and county for each.
    
    Parameters: file pointer, int, int
    return: float, str, float, str
    displays: nothing
    '''
    fp = reset_file_pointer_to_beginning(fp) #resets file to beginning
    header= fp.readline() #gets rid of the header line when reading
    min_val = 101 #setting minimum value first
    max_val = -1 #setting maximum value first
    
    for line in fp:
        value = float(line[start:end]) #slice involving start and end
        #for max's
        if value < min_val:
            min_val = value
            min_county = fix_county_string(line[24:43]) #which col for count
        #for min's
        if value > max_val:
            max_val = value
            max_county = fix_county_string(line[24:43])
        
    
    return min_val, min_county, max_val, max_county
    

def display_min_max(s,min_val, min_county, max_val, max_county):
    ''' 
    Calls the main function, the values are printed out in format for easy
    to read later on when run through the main function
    
    Parameters: str, str, str, str, str
    return: nothing
    displays: three lines as specified below
    '''
    
    
    print("\nPercent vaccinated for {}".format(s))
    
    print("\n\t Minimum is in {} at {}%".format(min_county, min_val))
    
    print("\t Maximum is in {} at {}%".format(max_county, max_val))
    
    
    
 
def all_vaccinated(fp):
    ''' 
    Resets the file pointer to the beginning, skips the header line, then 
    creates an empty list. Loops for each line in the file and adds that 
    all vaccinated value to the list as an int. When done iterating, the list
    of all vaccinated is then summed up, and returns the all vaccinated
    value
    
    Parameters: file pointer
    returns: int
    displays: nothing
    '''
    fp = reset_file_pointer_to_beginning(fp)
    
    header= fp.readline()
    
    #iterates each line in the file, grab value for vac, then change value to
    # int and add to the list
    
    allvac_list = []
    for line in fp:
        valuea_str = line[86:100]
        valuea_int = int(valuea_str)
        allvac_list.append(valuea_int)
    
    #sums up the list
    allvac_int = sum(allvac_list)
    
    return allvac_int
        
        
    
        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Minimum and Maximum of all vaccinated
    2: Minimum and Maximum of those 12 and older
    3: Minimum and Maximum of those 18 and older
    4: Minimum and Maximum of those 65 and older
    5: Total vaccinated for Michigan
    q: quit\n"""
    print(OPTIONS)
 

def main():
    ''' 
    The main function that calls the other functions in to process their 
    information. First the file is opened then the options for info are 
    displayed. User is prompted for input on thos options. Reprompts if input
    is invalid, will then process and return the wanted vaccine info 
    determined by the other functions. Reprompts user again if they would
    like to continue by asking for their input. Input of q will end the
    program
    
    Parameters: nothing
    returns: nothing
    displays: options and vaccine info based on prompts
    '''
    
    fp = open_file()
    display_options()
    
    option_str = input("Select and option, q to quit: ")
    
    #while not (option_str=='1' or option_str=='2' or option_str=='3' \
    #or option_str=='4' or option_str=='5' or option_str=='q'):
        #print("Invalid option; please try again.")
        #option_str = input("Select and option, q to quit: ")
    
    #loops until input of 'q' occurs 
    while option_str != 'q':
        
        #error checking to validate correct input of user
        while not (option_str=='1' or option_str=='2' or option_str=='3' \
        or option_str=='4' or option_str=='5' or option_str=='q'):
            print("Invalid option; please try again.")
            option_str = input("Select and option, q to quit: ")
        
        #while (option_str=='1' or option_str=='2' or option_str=='3' \
        #or option_str=='4' or option_str=='q'):

        #used for all vac value
        if option_str == '1':
            min_val, min_county, max_val, max_county = \
            find_min_max_column(fp, 71, 85)
            s = "all"
            display_min_max(s,min_val, min_county, max_val, max_county)
            display_options()
            option_str = input("Select and option, q to quit: ")
        
        #used for age 12 and older vac value    
        elif option_str =='2':
            min_val, min_county, max_val, max_county = \
            find_min_max_column(fp, 136, 154)
            s = "age 12 and older"
            display_min_max(s,min_val, min_county, max_val, max_county)
            display_options()
            option_str = input("Select and option, q to quit: ")
        
        #used for age 18 and older vac value
        elif option_str == '3':
            min_val, min_county, max_val, max_county = \
            find_min_max_column(fp, 183, 201)
            s = "age 18 and older"
            display_min_max(s,min_val, min_county, max_val, max_county)
            display_options()
            option_str = input("Select and option, q to quit: ")
        
        #used for age 65 and older vac value
        elif option_str == '4':
            min_val, min_county, max_val, max_county = \
            find_min_max_column(fp, 230, 234)
            s = "age 65 and older"
            display_min_max(s,min_val, min_county, max_val, max_county)
            display_options()
            option_str = input("Select and option, q to quit: ")
        
        #ends program
        elif option_str == 'q':
            break
        
        #gives value for total vac value in michigan
        elif option_str == '5':
            allvac_int = all_vaccinated(fp)
            print("\nTotal vaccinated in Michigan: {:,d}".format(allvac_int))
            display_options()
            option_str = input("Select and option, q to quit: ")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.         
if __name__ == "__main__":
    main()