##############################################################################
#       Computer Project #4
#
#       algorithm
#           function for banner
#           function for character input
#           main function that will call others and determine if laughing
#       print result of input of characters and if they are laughing
#
##############################################################################

import string



def print_banner():
    BANNER = '''                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""  '''
    print(BANNER)
    

#takes in input for character and verifies it is only one
def get_ch():
    ''' Remember the docstring'''
    
    value = False
    while value == False:
        ch = input("Enter a character or press the Return key to finish: ")
        ch = str(ch)
        if len(ch) ==1 or ch == '':
            if len(ch) <= 1:
                return True
            if ch == '':
                return True
        
        elif len(ch) > 1:
            print("Invalid input, please try again.")
            ch = input("Enter a character or press the Return key to finish: ")
            return False
print(get_ch()) 
#looping algorithm based on input of user, to determine if laughing
def find_state(state, ch):
    ''' Remember the docstring'''

    while state == 1:
        if ch == 'h':
            state = 2 
            return 2
        elif ch != 'h':
            state = 5
            return 5
        
    while state == 2:
        if ch =='a' or ch == 'o':
            state = 3
            return 3
        elif ch !='a' or ch != 'o':
            state = 5
            return 5
                
    while state == 3:
        if ch == 'h':
            state = 2
            return 2
        if ch == '!':
            state = 4
            return 4
        elif ch !='h' or ch !='!':
            state = 5
            return 5       
    while state == 4:
        if ch != '':
            state = 5
            return 5
    while state == 5:
        return 5
            
        
        
        
        
        
    
     
#calls both the find_state function and the get_ch function in
#defines variables and print out final results
def main():
    print_banner()
    print("I can recognize if you are laughing or not.\nPlease enter one character at a time.")
    ch = ''
    my_str=''
    state = 1
    state = int(state)

#    while state:
#        if state == 5:
#            print(my_str)
#            print("You are not laughing.")
        
#        elif state == 4:
#            print("\nYou entered", my_str)
#            print("You are laughing.")
        


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()