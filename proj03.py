##############################################################################
#   Computer Project #3
#
#       tuition calculator for undergrad msu
#           input grade level and validates input,error if wrong
#           input college if neccessary
#           input number of credits and validates input,error if wrong
#           calculates tuition based on input
#       displays tuition amount
#       asks if would like to repeat a new calculation
#
##############################################################################

#defining some variables here
eng_str = None
madison_str = None
none_str = None
health_str = None
sci_str = None
bus_str = None
answer = None
level = None
college = None # Don't define more than once, as above

#level, college, CoE_admitted,madison = None,None,None,None
print("2021 MSU Undergraduate Tuition Calculator.\n")
level = input("Enter Level as freshman, sophomore, junior, senior: ")
level = level.lower()
#print("level:",level) #for now clarification

#eng_str = None
#madison_str = None
#none_str = None
#health_str = None
#sci_str = None
#bus_str = None
#credits = input("Credits: ")
#credits = int(credits)
#print("Credits:",credits)
#level = None
#college = None # Don't define more than once, as above

#validating the input of the user to see if correct
while not(level=="freshman" or level=="sophomore" or level=="junior"or\
level=="senior"):
    #print(level)
    level = None
    print("Invalid input. Try again.")
    level = input("Enter Level as freshman, sophomore, junior, senior: ")
    if level=='freshman' or level=='sophomore' or level=='junior'\
or level=='senior':
        break
#main loop for calculating the tuition based on type
#starts by asking for college, madison college, etc. to organize 

while (level=='freshman') or (level=='sophomore') or (level=='junior')\
or (level=='senior') or (answer== 'yes'):
#    level = input("Enter Level as freshman, sophomore, junior, senior: ")
#    level = level.lower()    
    if level=='freshman' or level=='sophomore' or level=='junior'\
    or level=='senior':
        if level == 'junior' or level == 'senior':
            college_str =\
input("Enter college as business, engineering, health, sciences, or none: ")
            college_str = college_str.lower()
            #print("College:",college_str) #for now clarification
            if not(college_str=='business' or college_str=='engineering' or\
            college_str=='health' or college_str=='sciences'):
                college_str = input\
                ("Are you in the James Madison College (yes/no): ")
                college_str = college_str.lower()
                if college_str == 'yes':
                    madison_str = college_str
                if college_str != 'yes':
                    none_str = college_str
                    
            elif college_str == 'business':
                bus_str = college_str
            elif college_str == 'engineering':
                eng_str = college_str
            elif college_str == 'health':
                health_str = college_str
            elif college_str == 'sciences':
                sci_str = college_str
                
                
        
        if level == 'freshman' or level == 'sophomore':
            college_str = \
            input("Are you admitted to the College of Engineering (yes/no): ")
            if college_str == 'yes':
                #print(college_str)
                eng_str = college_str
            elif college_str != 'yes':
                college_str = \
                input("Are you in the James Madison College (yes/no): ")
                if college_str == 'yes':
                    #print(college_str)
                    madison_str = college_str
                elif college_str != 'yes':
                    #print(college_str)
                    none_str = college_str
                    
        
                    
        
        # if frosh or soph, ask to admit to Eng -> CoE_admitted
        # if not ..., ask Madison -> madison 
        
#print("level, college, CoE_admitted,madison ->",level, college,CoE_admitted,\
        #      madison)
        
        
            
        credits = input("Credits: ")
        while not credits.isdigit() or not int(credits) > 0:
            print("Invalid input. Try again.")
            credits = input("Credits: ")
            if credits.isdigit():
                break
        credits = int(credits)
        #print("Credits:",credits)
        ###################################
        
        if 6 <= credits <= 11: # part time credits (1-11)
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 5 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 5 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 5 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 5 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 5 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 5 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 5 + 100
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3 + 5
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition = 573*credits + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
#the flat rates from 12-18 credits(closed interval)                    
        if 12 <= credits <= 18: 
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 7230 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition = 7230 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuiton_str = 7230 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7230 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            if level == 'sophomore':
                if eng_str:
                    tuition_str = 7410 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7410 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7410 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'junior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 100 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
        # flat + credit where credits are greater than 18
        if 18 < credits:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 7230 + 482*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7230 + 482*(credits-18) + 21 + 3 + 5 + 7.5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7230 + 482*(credits-18) + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'sophomore':
                if eng_str:
                    tuition_str = 7410 + 494*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7410 + 494*(credits-18) + 21 + 3 + 5 + 7.5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7410 + 494*(credits-18) + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            if level == 'junior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 555*(credits-18) + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 573*(credits-18) + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 573*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 555*(credits-18) + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 573*(credits-18) + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 573*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
        # special cases
        if credits == 5:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 100
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3  
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3 
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 100 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
            
        # part time, 4 credits or less
        if 1 <= credits <= 4:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 402 + 21 + 3 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 402 + 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 113 + 21 + 3  
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 402 + 21 + 3 
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 50 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 113 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition = 573*credits + 402 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
        answer = input("Do you want to do another calculation (yes/no): ")
        answer = answer.lower()
        if answer != 'yes':
            break
                    
                
                    
##########################################################
#repeated loop is would like to calculate tuition again 
   
    if answer == 'yes':
        level = input("Enter Level as freshman, sophomore, junior, senior: ")
        level = level.lower()
        while not(level=="freshman" or level=="sophomore" or\
        level=="junior"or level=="senior"):
            #print(level)
            level = None
            print("Invalid input. Try again.")
            level = \
            input("Enter Level as freshman, sophomore, junior, senior: ")
            if level=='freshman' or level=='sophomore' or level=='junior'\
or level=='senior':
                break
       
        if level == 'junior' or level == 'senior':
            college_str =\
input("Enter college as business, engineering, health, sciences, or none: ")
            college_str = college_str.lower()
            #print("College:",college_str) #for now clarification
            if not(college_str=='business' or college_str=='engineering' or\
            college_str=='health' or college_str=='sciences'):
                college_str = \
                input("Are you in the James Madison College (yes/no): ")
                college_str = college_str.lower()
                if college_str == 'yes':
                    madison_str = college_str
                if college_str != 'yes':
                    none_str = college_str
                    
            elif college_str == 'business':
                bus_str = college_str
            elif college_str == 'engineering':
                eng_str = college_str
            elif college_str == 'health':
                health_str = college_str
            elif college_str == 'sciences':
                sci_str = college_str
                
                
        
        if level == 'freshman' or level == 'sophomore':
            college_str = \
            input("Are you admitted to the College of Engineering (yes/no): ")
            if college_str == 'yes':
                #print(college_str)
                eng_str = college_str
            elif college_str != 'yes':
                college_str = \
                input("Are you in the James Madison College (yes/no): ")
                if college_str == 'yes':
                    #print(college_str)
                    madison_str = college_str
                elif college_str != 'yes':
                    #print(college_str)
                    none_str = college_str
                    

        # if frosh or soph, ask to admit to Eng -> CoE_admitted
        # if not ..., ask Madison -> madison 
        
#print("level, college, CoE_admitted,madison ->",level, college,CoE_admitted,
        #      madison)
        
        
            
        credits = input("Credits: ")
        while not credits.isdigit() or not int(credits) > 0:
            print("Invalid input. Try again.")
            credits = input("Credits: ")
            if credits.isdigit():
                break
        credits = int(credits)
        #print("Credits:",credits)
        ###################################
        
        if 6 <= credits <= 11: # part time credits (1-11)
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 5 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 5 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 5 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 5 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 5 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 5 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 5 + 100
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3 + 5
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition = 573*credits + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))

#the flat rates from 12-18 credits(closed interval)                    
        if 12 <= credits <= 18: 
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 7230 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition = 7230 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuiton_str = 7230 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7230 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            if level == 'sophomore':
                if eng_str:
                    tuition_str = 7410 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7410 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7410 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'junior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 100 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
        # flat + credit where credits are greater than 18
        if 18 < credits:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 7230 + 482*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7230 + 482*(credits-18) + 21 + 3 + 5 + 7.5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7230 + 482*(credits-18) + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'sophomore':
                if eng_str:
                    tuition_str = 7410 + 494*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 7410 + 494*(credits-18) + 21 + 3 + 5 + 7.5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 7410 + 494*(credits-18) + 21 + 3 + 5 
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            if level == 'junior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 555*(credits-18) + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 573*(credits-18) + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 573*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
            if level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 8325 + 555*(credits-18) + 100 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 8595 + 573*(credits-18) + 226 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 8595 + 573*(credits-18) + 670 + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 8325 + 555*(credits-18) + 21 + 3 + 5
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                    
        # special cases
        if credits == 5:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 670 + 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 100
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3  
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3 
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 100 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 226 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 670 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
            
        # part time, 4 credits or less
        if 1 <= credits <= 4:
            
            if level == 'freshman':
                
                if eng_str:
                    tuition_str = 402 + 21 + 3 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 482*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + (482*credits)
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                        
            elif level == 'sophomore':
                
                if eng_str:
                    tuition_str = 402 + 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif madison_str:
                    tuition_str = 21 + 3 + 7.50 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 21 + 3 + 494*credits
                    #print(tuition_str)
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'junior':
                
                if health_str or sci_str:
                    tuition_str =  555*credits + 21 + 3 + 50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 113 + 21 + 3  
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition_str = 573*credits + 402 + 21 + 3 
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                
            elif level == 'senior':
                
                if health_str or sci_str:
                    tuition_str = 555*credits + 50 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if bus_str:
                    tuition_str = 573*credits + 113 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if eng_str:
                    tuition = 573*credits + 402 + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                if madison_str:
                    tuition_str = 555*credits + 21 + 3 + 7.50
                    print("Tuition is ${:,.2f}.".format(tuition_str))
                elif none_str:
                    tuition_str = 555*credits + 21 + 3
                    print("Tuition is ${:,.2f}.".format(tuition_str))
        
        #    elif level ==
        #print("Do you want to do another calculation (yes/no): ")
        #asking to repead loop to calculate
        answer = input("Do you want to do another calculation (yes/no): ")
        answer = answer.lower()
        if answer != 'yes':
            break