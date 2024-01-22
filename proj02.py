##############################################################################
#   Computer Project #2
#       algorithm to calculate car rental cost in Forza
#           prompted if you would like to continue with service
#           input customer code for rate on such code/deal
#           input miles on odometer(start/end) and days rented
#           calculate amount due after rental
#       display details on rental price and facts
#
##############################################################################

BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
 
PROMPT = '''\nWould you like to continue (A/B)? '''
SUMMARY = "\nCustomer summary:"
CC = "\tclassification code:"
PERIOD = "\trental period (days):"
START = "\todometer reading at start:"
END = "\todometer reading at end:  "
MILES = "\tnumber of miles driven: "
DUE = "\tamount due: $"
INVALID = "\n\t*** Invalid customer code. Try again. ***"
CUSTOMER_CODE = "\nCustomer code (BD, D, W): "
print(BANNER)

import math

choice_str = input(PROMPT)
#code_str = input(CUSTOMER_CODE)
while choice_str == "A": # given choice to continue
    #print(choice_str) # might be unneccessary
    CUSTOMER_CODE = "\nCustomer code (BD, D, W): "
    code_str = input(CUSTOMER_CODE)
    #choice_str = input(PROMPT)
    if code_str == "BD": # calculation for budget rate
        DAYS = "\nNumber of days: "
        days_str = input(DAYS)
        days_int = int(days_str)
        milesbeg_str = input("Odometer reading at the start: ")
        milesbeg_int = int(milesbeg_str)
        milesend_str = input("Odometer reading at the end:   ")
        milesend_int = int(milesend_str)
        
        if milesend_int < milesbeg_int:
            miles_int = ((1000000-milesbeg_int) + milesend_int)*(10**(-1))
        else:
            miles_int = (milesend_int - milesbeg_int)*(10**(-1)) 
        
        due_int = 40.00*days_int + 0.25*miles_int
        
        print(SUMMARY)
        print(CC,"BD")
        print(PERIOD, days_int)
        print(START,milesbeg_int)
        print(END,milesend_int)
        print(MILES, round(miles_int,1))
        print(DUE,round(due_int,2))
    
        choice_str = input(PROMPT)
    
    if code_str == "D": # Daily rate calculations
        DAYS = "\nNumber of days: "
        days_str = input(DAYS)
        days_int = int(days_str)
        milesbeg_str = input("Odometer reading at the start: ")
        milesbeg_int = int(milesbeg_str)
        milesend_str = input("Odometer reading at the end:   ")
        milesend_int = int(milesend_str)
        
        if milesend_int < milesbeg_int:
            miles_int = ((1000000-milesbeg_int) + milesend_int)*(10**(-1))
        else:
            miles_int = (milesend_int - milesbeg_int)*(10**(-1))
            
        avgmiles_int = (miles_int/days_int)
        
        if avgmiles_int <= 100:
            due_int = 60.00*days_int
            
        if avgmiles_int > 100:
            due_int = 60.00*days_int + 0.25*(miles_int-(days_int*100))
            
        print(SUMMARY)
        print(CC,"D")
        print(PERIOD,days_int)
        print(START,milesbeg_int)
        print(END,milesend_int)
        print(MILES,round(miles_int,1))
        print(DUE,round(due_int,2))
    
        choice_str = input(PROMPT)
    
    if code_str == "W": # calculation for weekly rate
        DAYS = "\nNumber of days: "
        days_str = input(DAYS)
        days_int = int(days_str)
        milesbeg_str = input("Odometer reading at the start: ")
        milesbeg_int = int(milesbeg_str)
        milesend_str = input("Odometer reading at the end:   ")
        milesend_int = int(milesend_str)
        
        if milesend_int < milesbeg_int:
            miles_int = ((1000000-milesbeg_int) + milesend_int)*(10**(-1))
        else:
            miles_int = (milesend_int - milesbeg_int)*(10**(-1))
        
        wks_int = math.ceil(days_int/7) 
        
        avgmiles_int = (miles_int/wks_int)
        
        if round(avgmiles_int) <= 900:
            due_int = 190.00*wks_int
        
        if avgmiles_int > 900 or avgmiles_int <= 1500:
            due_int = 190*wks_int + 100.00*wks_int
            
        if avgmiles_int > 1500:
            due_int =190*wks_int +200*wks_int +0.25*(miles_int-(wks_int*1500))
        
        print(SUMMARY)
        print(CC,"W")
        print(PERIOD,days_int)
        print(START,milesbeg_int)
        print(END,milesend_int)
        print(MILES,round(miles_int,1))
        print(DUE,round(due_int,2))
        
        choice_str = input(PROMPT)
        
    #inv_str = input(INVALID)
    
    #code_str == input(CUSTOMER_CODE)
    while not(code_str == "BD" or code_str == "D" or code_str == "W"):
        print(INVALID)
        code_str = input(CUSTOMER_CODE)
        
        
        
            
    #inv_str = input(INVALID)
    
    #code_str = input(CUSTOMER_CODE)
    
    #choice_str = input(PROMPT)
    
#choice_str = input(PROMPT)
        
        
        
        
            
if choice_str != "A":
    print("Thank you for your loyalty.")