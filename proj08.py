##############################################################################
#   Computer Project #8
#   
#   algorithm that reads a data.csv file with info for regions, and countries
#   that also contains values for certain categories
#       reads file and gathers data
#       organizes data into a dictionary
#       asks user for region on wanted info
#       displays and asks user more options on what to do with info from that
#       region
#       asks the user if they would like to continue or not, and on that 
#       region or a new region
#   ends the program if user enters 'q' or 'Q' when prompted
##############################################################################









import csv
from operator import itemgetter
# do NOT import sys

REGION_LIST = ['East Asia & Pacific',
                'Europe & Central Asia',
                'Latin America & Caribbean',
                'Middle East & North Africa',
                'North America',
                'South Asia',
                'Sub-Saharan Africa']

PROMPT = "\nSpecify a region from this list or 'q' to quit -- \nEast Asia & Pacific,Europe & Central Asia,Latin America & Caribbean,Middle East & North Africa,North America,South Asia,Sub-Saharan Africa: "

def open_file():
     '''
    Asks the user to input a file to use, if not correct, reprompts user for 
    valid file input until correct
    
    Parameters: None
    return: file_pointer
    displays: prompt and error message as appropriate 
    '''
     #pass # replace this command with your code
     
     
     file_str = input('Input a file: ')
     while True:
         try:
                 fp = open(file_str, "r")
                 return fp
            
         except FileNotFoundError:
            print('Invalid filename, please try again.')
            file_str = input('Input a file: ')

def read_file(fp):
     '''
     Creates a dictionary and then reads through the csv file given. It then
     iterates through the file and assigns variables to specified values in
     the list from reader. It then adds to the dictionary with the region as
     the key for the list of new variables. Continues if the region is empty
     Parameters: file pointer
     returns: dictionary
     displays: None
     '''
     #pass # replace this command with your code
     #create a dictionary and read through the file
     Dict = {}
     reader = csv.reader(fp)
     for row_list in reader:
         
         #try to assign variable and float specified values
         try:
             name = row_list[0].strip()
             region = row_list[6].strip()
             elec = float(row_list[2])
             fert = float(row_list[3])
             GDP = float(row_list[4])
             life = float(row_list[5])
             #create list with new variable
             L = [name,elec,fert,GDP,life]
             # put it in a dictionary
             
             if region == "":
                 continue
             
             elif region not in Dict:
                 Dict[region] = []
                 Dict[region].append(L)
                 
             else:
                 Dict[region].append(L)
                 
             
         except ValueError:
            pass
        
     return Dict

def get_min_max(D, region, option):
     '''
     This function gets the minimum and maximum for a specified value of a 
     specified region in the dictionary. It then adds these values(dependent 
     on option) to the new list. It sorts this and returns the max and min
     country with their associating values in a tuple.
     Parameters: dictionary, region(str), option(int)
     returns: min_tuple, max_tuple
     displays: None
     '''
     #pass # replace this command with your code
     
     # if region not in REGION_LIST:
         
     #     return (None,None)
     
     # elif option!=1 or option!=2 or option!=3 or option!=4:
         
     #     return (None,None)
     
     #create a list for the values
     values_lst = []
     #error checking the inputs
     if not region in D or not 1<=option<=4:
         return None, None
         
     for values in D[region]:
         
       
       #sort by electricty first          
        if option == 1:
            elec = values[1]
            values_lst.append((elec,values[0]))
        #sort by fertility
        if option == 2:
            fert = values[2]
            values_lst.append((fert,values[0]))
        #sort by GDP
        if option == 3:
            GDP = values[3]
            values_lst.append((GDP,values[0]))
        #sort by life expectancy    
        if option == 4:
            life = values[4]
            values_lst.append((life,values[0]))
            
    
                
     sorted_val = sorted(values_lst)
     #print(sorted_val)
     max_value = sorted_val[-1]
     
     min_value = sorted_val[0]
     
     return_max = (max_value[1],max_value[0])
     
     return_min = (min_value[1],min_value[0])
     #print(return_max)
     return (return_min,return_max)
    
    

             
          
    
def display_all_countries(D,region):
     '''
     Displays the region, then displays the header and the values associated
     with each country in the region and formats it to look nice, it also 
     sorts this dictionary and country and alphabetical order and prints them
     Parameters: dictionary, region(str)
     returns: none
     displays: all the countries in a region
     '''
     #pass # replace this command with your code
     
     print("\nDisplaying {} Region:".format(region))
     
     #skip a line, then print header
     
     print("{:32s}{:>20s}{:>20s}{:>17s}{:>18s}".format\
          ('Country', 'Electricity Access', 'Fertility rate','GDP per capita',\
           'Life expectancy'))
     
     for key,value in D.items():
         #country = i[0]
         print("{:32s}{:>20.2f}{:>20.2f}{:>17.2f}{:>18.2f}".format(region,value))

def get_top10(D):
     '''
     This function gets the top 10 countries for GDP in all the regions and
     puts them into a list of tuples with the top 10's.
     Parameters: dictionary
     returns: list of tuples
     displays: None
     '''
     #pass # replace this command with your code
     
     country_list = []
     
     for key in D:
         #print(key,value)
         country = key[0]
         country_list.append((country,key[3]))
    
     c_max_min = sorted(country_list, reverse = True)
     top_ten = []
     for i in c_max_min[:9]:
         top_ten.append(i)
         
     return top_ten
         
        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Minimum and Maximum Countries Access to Electricity
    2: Minimum and Maximum Countries Fertility Rate
    3: Minimum and Maximum Countries GDP per Capita
    4: Minimum and Maximum Countries Life Expectancy
    5: List of countries in a region
    6: Top 10 Countries in the world by GDP per Capita\n"""
    print(OPTIONS)


def main():
     '''
     This is the main function for the program. It runs the other functions of
     the program within it. It takes what options are given to it in and uses
     the functions correlating to it. To the end the program, enter q or Q.
     Parameters: none
     returns: none
     displays: none
     '''
     #pass # replace this command with your code
         
     fp = open_file()
     D = read_file(fp)
   #  get_min_max(D, region, option)
     region_str = input(PROMPT)
     if region_str == 'q':
         pass
     
     while region_str != 'q' or region_str != 'Q':
         
          # while not (region_str == 'East Asia & Pacific',\
          # region_str == 'Europe & Central Asia',\
          # region_str == 'Latin America & Caribbean', region_str == 'Middle East & North Africa', region_str == 'North America', region_str == 'South Asia', region_str == 'Sub-Saharan Africa'):
          while region_str not in REGION_LIST and not(region_str=='q' or region_str=='Q'):
                                                      
              region_str = input(PROMPT)
             
          print("\nRegion:",region_str)
          display_options()
          option_str = input('\nChoose an option, R to select a different region, q to quit: ')
          
          if option_str == '1':
              min_val,max_val = get_min_max(D, region_str, option_str)
              print("\n{:s} has the highest access to electricity of {:.2f}%".format(region_str,max_val))
              
              print("{:s} has the lowest access to electricity of {:.2f}%".format(region_str,min_val))
              
              option_str = input('\nChoose an option, R to select a different region, q to quit: ')
              
         
             
             
             
             
             
          if region_str == 'q' or region_str == 'Q' or option_str =='q':
              break
     if region_str =='q':
         pass
     
     
     

if __name__ == '__main__':
    main()
