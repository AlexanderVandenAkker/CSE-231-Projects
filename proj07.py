##############################################################################
#   Computer Project #7
#       algorithm that takes in a csv file of sales/revenue
#           reads file and gathers data
#           organizes that data
#           asks user for option on wanted information
#           gathers the info for the option and displays for user
#           asks if would like to plot received data or not
#           reprompts user to continue with different option
#       ends the program if the user decides on option '4'
##############################################################################    











#sales_revenue_2007_2020.csv

import csv
import matplotlib.pyplot as plt


CATEGORIES = ["Residential", "Commercial", "Industrial", "Transportation"]
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def open_file():
    ''' 
    Asks the user to input a file to use, if not correct, reprompts user for 
    valid file input until correct
    
    Parameters: None
    return: file_pointer
    displays: prompt and error message as appropriate
    '''
#    pass
    
    file_str = input("Enter filename: ")
    while True:
        try:
            fp = open(file_str, "r")
            return fp
            
        except FileNotFoundError:
            print("The file cannot be found! Please Try Again!!!")
            file_str = input("Enter filename: ")

def convert_data(lst):
    '''
    Takes in a list of strings, and converts the first three strings into 
    an int, the last string is converted to a float, this funciton then 
    returns these values in a new list
    Parameters: List of size four(list of strings)
    returns: List of size four(list of ints and float)
    '''
    new_lst = []
    
    rev = lst[0]
    rev = rev.replace(",","")
    rev_int = int(rev)
    new_lst.append(rev_int)
    
    sales = lst[1]
    sales = sales.replace(",","")
    sales_int = int(sales)
    new_lst.append(sales_int)
    
    cust = lst[2]
    cust = cust.replace(",","")
    cust_int = int(cust)
    new_lst.append(cust_int)
    
    price = lst[3]
    if price=="" or price ==".":
        price = "0"
    else:
        price = price.replace(",","")
    price_flt = float(price)
    new_lst.append(price_flt)
    
    return new_lst
    
    
    
    
def read_file(fp):
    '''
    Reads the csv file that is inputed, and also creates four tuples
    corresponding to it's appropriate category. It then iterates through each
    line in the file, and appropriately applies the information to their
    respecting tuple. After organizing these, it then creates a master list
    and appends the categorized and organized tuples to that master list and
    returns it
    Parameters: File pointer object
    returns: list(list(tuple), list(tuple), list(tuple), list(tuple))
    '''
    #pass
    reader = csv.reader(fp)
    
    #skipping 3 lines in the file
    next(reader,None)
    next(reader, None)
    next(reader, None)
    
    #create a master list, has list(list(tup),list(tup),list(tup),list(tup))
    
    
    res_lst = []
    com_lst = []
    ind_lst = []
    trans_lst = []
    
    
    #call convert_data(lst) to help change values somehow?
    #go through each line and split it on comma
    for line in reader:        
        year = line[0]
        year = int(year)
        state = line[1]
        
        res = convert_data(line[3:7])
        
        com = convert_data(line[7:11])
        
        ind = convert_data(line[11:15])
        
        trans = convert_data(line[15:19])
        
        res_tup = (year,state,res[0],res[1],res[2],res[3])
        res_lst.append(res_tup)
        
        com_tup = (year,state,com[0],com[1],com[2],com[3])
        com_lst.append(com_tup)
        
        ind_tup = (year,state,ind[0],ind[1],ind[2],ind[3])
        ind_lst.append(ind_tup)
        
        trans_tup = (year,state,trans[0],trans[1],trans[2],trans[3])
        trans_lst.append(trans_tup)
        
    master_lst = [res_lst,com_lst,ind_lst,trans_lst]
    return master_lst
        
        
       
        
    
    

def get_year_or_state_data(L, index, value):
    '''
    Creates a new list depending on whether it is the year or state. Then 
    append the appropriate line to the new list
    Parameters: list(tuple), int, int or str (depending on the index)
    Returns: list(tuple)
    '''
    #L = read_file(fp)
    new_list = []
    if index == 0:   #YEAR
    #       loop tup through L:
        for line in L:
            if line[0] == value:
    #               append tup on to new_list
                new_list.append(line)
    elif index == 1:     #STATE
        for line in L:
            if line[1] == value:
                new_list.append(line)
    
    return new_list

def display_year_or_state_data(L,index,title):
    '''
    Displays all the data in categories bases on their years or states
    Prints the information in a way that is readable to the user
    Parameters: list(tuples), int, str
    Returns: None
    '''
    
    print("{:^80s}".format(title))
    
    if index == 0:
        print(("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format\
             ("Year","Revenue","Sales","Number of Customers","Price")))
            
    elif index == 1:
        print(("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format\
             ("State","Revenue","Sales","Number of Customers","Price")))
            
    print(("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format\
         ("","(in Thousands)","(MWh)","","(Cents/kWh)")))
    
    for line in L:
        start = line[index]
        start = str(start)
        print("{:>5s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format\
             (start,line[2],line[3],line[4],line[5]))
        
def get_totals(master_list):
    '''
    Gets the totals for each of the categories and appends them to the totals
    list. It also rounds the price to 2 decimal places
    Parameters: list(list(tuples))
    Returns: list(list( (int, int, int, float) ))
    '''
    totals_list = []
    
    for line in master_list:
        lst = [0,0,0,0]
        
        for i in line:
            
            lst[0] += i[2]
            
            lst[1] += i[3]
            
            lst[2] += i[4]
            
            lst[3] += i[5]
            
        lst[3] = round(lst[3]/len(line),2)
        
        totals_list.append(lst)
        
    return totals_list
        

def display_totals(L):
    '''
    Displays the totals for each of the the categories and prints the info
    in a way that is readable to the user, depending on the category
    of in input
    Parameters: list(list)
    Returns: None
    '''
    ##what do i put for first title
    print("{:^80s}".format("Revenue/Sales total for each category"))
    
    
    print("{:>15s}{:>18s}{:>18s}{:>22s}{:>14s}".format\
         ("Category","Revenue","Sales","Number of Customers","Price"))
        
    print("{:>15s}{:>18s}{:>18s}{:>22s}{:>14s}".format\
         ("","(in Thousands)","(MWh)","","(Cents/kWh)"))
    
    for ind,line in enumerate(L):
        if ind == 0:
            print("{:>15s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format\
                 ("Residential",line[0],line[1],line[2],line[3]))
        elif ind == 1:
            print("{:>15s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format\
                 ("Commercial",line[0],line[1],line[2],line[3]))
        elif ind == 2:
            print("{:>15s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format\
                 ("Industrial",line[0],line[1],line[2],line[3]))
        elif ind == 3:
            print("{:>15s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format\
                 ("Transportation",line[0],line[1],line[2],line[3]))
            
        

def state_plots(data,label):
    '''
        DO NOT MODIFY/DELETE THIS FUNCTION! 
        
        This function generates the plots for each column for a single area across
        every year for a single state.
        
        Parameters:
            data (list): The list of tuples with the sales/revenue tuples.
            label (str): State value for the tuples in data.
            
        Returns:
            None
    '''

    index = 0
    x_label = "year"
    
    x_labels = [str(y[index]) for y in data]
    revenue = [y[2] for y in data]
    sales = [y[3] for y in data]
    customers = [y[4] for y in data]
    price = [y[5] for y in data]
    
    form = "{} in {}".format("years",label)
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,15))

    
    #Plot the revenue and the sales in different y axes
    title = "Revenue and Sales per " + form
    y1_label = "Revenue (In Thousands)"
    y2_label = "Sales (MWh)"
    plot_line(axes[0],x_labels, [revenue,sales], title,[y1_label,y2_label],["Revenue","Sales"])
    axes[0].xaxis.set_ticklabels([])
    
    #Plot the number of customer and prices in different y axes
    title = "Number of customer and prices per " + form
    y3_label = "Number of customers"
    y4_label = "Price (Cents/kWh)"
    plot_line(axes[1],x_labels, [customers,price], title,[y3_label,y4_label],["Customer","Price"])
    axes[1].set_xlabel(x_label)

    fig.tight_layout()#automatically adjusts the positions of the axes so that
                  #there is no overlapping content:
    plt.show()
    


def plot_line(ax,x, y, title, y_label,legend):
    '''
        DO NOT MODIFY/DELETE THIS FUNCTION! 
        
        This function generates a line plot.
        
        Parameters:
            ax (matplotlib.axes._subplots.AxesSubplot): handle for figure axes
            x (list): List of x value strings for the line plot
            y (list): List of list of y values for the two Y-axes
            title (str): the title for the graph
            x_label (str): Name of the x-axis
            y_label (list): List of Names of the y-axis
            legend (list): List of names of the curves
            
            
        Returns:
            None
    '''
    
    ax.plot(x, y[0],label = legend[0],color="blue") #lw is line width
    ax.set_ylabel(y_label[0])
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.xaxis.set_ticklabels([])    
    for labels in ax.get_yticklabels():
        labels.set_color("blue")
        
    ax2 = ax.twinx()
    ax2.plot(x, y[1],label = legend[1],color="red")
    ax2.set_ylabel(y_label[1])    
    ax2.legend(loc='upper right')

    for labels in ax2.get_yticklabels():
        labels.set_color("red")

def main():
    
    BANNER = ''' Revenue/Sales data of Electricity in the United States across different areas: 
        Residential, Commercial, Industrial, and Transportation.'''
    print(BANNER)
    
    # Menu of the program
    MENU = '''Menu
    
    1. Display Revenue/Sales in a year
    2. Display Revenue/Sales in a state
    3. Display Total Revenue/Sales per category
    4. Stop the program
    
    Enter your option: '''
    
    #print("Thank you for using this program!")
    
    fp = open_file()
    master_lst = read_file(fp) #????
    option_str = input(MENU)
    
    
    
    
    
    # #loops until input of '4' occurs 
    while option_str != '4':
    
        
    #instead of option_str do i call the menu somehow?
    #     #error checking to validate correct input of user
        while not (option_str=='1' or option_str=='2' or option_str=='3' \
        or option_str=='4'):
             print("Invalid option!")
             option_str = input(MENU)
             
        if option_str == "1":
            cat_str = input("Enter category: ")
            cat_str = cat_str.capitalize()
            while cat_str not in CATEGORIES:
                print("Invalid category! ")
                cat_str = input("Enter category: ")
            year_str = input("Enter year (2007-2020): ")
            while not (year_str.isdigit()) or int(year_str)<2007 or\
            int(year_str)>2020:
                 print\
                ("Incorrect year! The year has to be between 2007 and 2020!")
                 year_str = input("Enter year (2007-2020): ")
            
            year_str = int(year_str)
            
            if cat_str == "Residential":
                
                new_list = get_year_or_state_data(master_lst[0],0,year_str)
                display_year_or_state_data\
                (new_list,0,"{} revenue/sales in {}".format(cat_str,year_str))
                

            
            elif cat_str == "Commercial":
                new_list = get_year_or_state_data(master_lst[1],0,year_str)
                display_year_or_state_data\
                (new_list,0,"{} revenue/sales in {}".format(cat_str,year_str))
                

                
            elif cat_str == "Industrial":
                new_list = get_year_or_state_data(master_lst[2],0,year_str)
                display_year_or_state_data\
                (new_list,0,"{} revenue/sales in {}".format(cat_str,year_str))
                

                
            elif cat_str == "Transportation":
                new_list = get_year_or_state_data(master_lst[3],0,year_str)
                display_year_or_state_data\
                (new_list,0,"{} revenue/sales in {}".format(cat_str,year_str))
                

            
            option_str = input(MENU)
                
                
            
                
            
            
        
        elif option_str == "2":
            cat_str = input("Enter category: ")
            cat_str = cat_str.capitalize()
            while cat_str not in CATEGORIES:
                print("Invalid category! ")
                cat_str = input("Enter category: ")
            state_str = input("Enter state: ")
            while state_str not in STATES:
                print("Invalid state!")
                state_str = input("Enter state: ")
                
            if cat_str == "Residential":
                
                new_list = get_year_or_state_data(master_lst[0],1,state_str)
                display_year_or_state_data\
                (new_list,1,"{} revenue/sales in {}".format(cat_str,state_str))
            
                
            elif cat_str == "Commercial":
                
                new_list = get_year_or_state_data(master_lst[1],1,state_str)
                display_year_or_state_data\
                (new_list,1,"{} revenue/sales in {}".format(cat_str,state_str))

                
            elif cat_str == "Industrial":
                new_list = get_year_or_state_data(master_lst[2],1,state_str)
                display_year_or_state_data\
                (new_list,1,"{} revenue/sales in {}".format(cat_str,state_str))
            
                
            elif cat_str == "Transportation":
                new_list = get_year_or_state_data(master_lst[3],1,state_str)
                display_year_or_state_data\
                (new_list,1,"{} revenue/sales in {}".format(cat_str,state_str))
            

                
            plot_str = input("Do you want to plot (y/n)?")
            plot_str = plot_str.lower()
            if plot_str == 'y':
                state_plots(new_list, state_str)
            option_str = input(MENU)
            
                
        
        
        elif option_str == "3":
            new_list22 = get_totals(master_lst)
            #print(new_list22)
            display_totals(new_list22)
            
            option_str = input(MENU)
            
    
        
    
    
        elif option_str == '4':
            break
            
    
    print("Thank you for using this program!")
    
        
            

# DO NOT DELETE THESE TWO LINES
if __name__ == "__main__":
    main()