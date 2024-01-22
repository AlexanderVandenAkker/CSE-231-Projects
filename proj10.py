##############################################################################
#   Computer Project #10
#       program that runs the solitaire game of shamrocks!
#           prints a welcome message and initializes the game
#           displays tableau and foundation using display()
#           prints the menu for the user to see
#           prompts user for option using get_option() function
#           checks users input for option, and runs if valid!
#           displays info for option, if not valid displays invalid option and
#               reprompts the user for option
#           if user eventually wins, prints a victory message and restarts the 
#               game
#       upon entering 'q' for option quits game and displays goodbye message
##############################################################################








#DO NOT DELETE THESE LINES

import cards, random, copy
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from end of Tableau pile s to end of pile d.
    MTF s d: Move card from end of Tableau pile s to Foundation d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

  
def fix_kings(tableau):
    '''
    This function takes in a tableau which is a lists of lists, with three
    cards each and the last list having only one. This function then converts
    each stack of cards in tableau(if needed) to make sure kings all come
    first to in each stack
    Parameters: tableau (list of lists)
    returns: none
    displays: none
    '''
    #pass    # replace this line with your code
    
    #iterates through tableau for each stack
    for stack in range(len(tableau)):
        
        #if last stack of one, no need for process so break
        if stack == 17:
            break
        
        #if first card is not king and second is, move first card to front of 
        # list
        if tableau[stack][0].rank() != 13 and tableau[stack][1].rank() == 13:
            
            card = copy.deepcopy(tableau[stack][0]) 
            tableau[stack][0] = tableau[stack][1]
            tableau[stack][1] = card
        
        #if second card is not king and third is, move second card to front of 
        # list
        if tableau[stack][1].rank() != 13 and tableau[stack][2].rank() == 13:
            
            card = copy.deepcopy(tableau[stack][1]) 
            tableau[stack][1] = tableau[stack][2]
            tableau[stack][2] = card
        
            
        #if first card is not king and second is, move first card to front of 
        # list(repeats first to cover case of third card slot) 
        if tableau[stack][0].rank() != 13 and tableau[stack][1].rank() == 13:
            
            card = copy.deepcopy(tableau[stack][0]) 
            tableau[stack][0] = tableau[stack][1]
            tableau[stack][1] = card
        
        
                
def initialize():
    '''
    This function initializes the game by creating the foundation for the game
    and the tableau which is a list of lists(the stacks of cards). It then 
    creates a deck and shuffles it, dealing them to the stacks in the tableau.
    Once done dealing, it calls the fix_kings() function to make sure the
    the kings are ordered right.
    Parameters: none
    returns: tableau(list of eighteen lists), foundation(list of four lists)
    displays: none
    '''
    #pass    # replace this line with your code
    #initialize foundation and tableau lists, create deck and shuffle it
    foundation = [[],[],[],[]]
    tableau = []
    deck = cards.Deck()
    deck.shuffle()
    
    #create new list for each stack
    for stack in range(18):
        
        sta = []
        #if last stack add card and break
        if stack == 17:
            sta.append(deck.deal())
            tableau.append(sta)
            break
        
        
        #deal three cards to each stack in the tableau
        for i in range(3):
            
            sta.append(deck.deal())
            
        tableau.append(sta)
        
    
    #clean up and move kings to front by calling function
    fix_kings(tableau)
    
    #return the tableau and foundation
    return tableau, foundation
        

def get_option():
    '''
    This function prompts the user to input an option, it then validates if 
    the option is correct and returns the associated value with it as a list.
    Parameters: None
    returns: list of 1 0r 3 containing the input
    displays: none
    '''
    #pass    # replace this line with your code
    
    #prompts user for an input on option, splits on whitespace to make list
    option_str = input("\nInput an option (MTT,MTF,U,R,H,Q): ")
    option_split = option_str.split()
    
    #single letter inputs, returns it if one of the options
    if option_str.upper() == 'U':
        return ["U"]
    elif option_str.upper() == 'R':
        return ["R"]
    elif option_str.upper() == 'H':
        return ["H"]
    elif option_str.upper() == 'Q':
        return ["Q"]
    
    #checks if list is length 3, proceeds if it is
    elif len(option_split) == 3:
        
        #checks if 2nd and third slot in list is a number
        if not option_split[1].isnumeric():
            print("Error in option: {}".format(option_str))
            return None
            
        if not option_split[2].isnumeric():
            print("Error in option: {}".format(option_str))
            return None
            
        
        #changes the numbers to integers
        option_split[1] = int(option_split[1])
        option_split[2] = int(option_split[2])
        
        #checks the first string in the list
        if option_split[0].upper() == 'MTT':
            return option_split
        elif option_split[0].upper() == 'MTF':
            return option_split
        else:
            print("Error in option: {}".format(option_str))
            return None
            
    
    else:
        print("Error in option: {}".format(option_str))
        return None
        
          
def valid_tableau_to_tableau(tableau,s,d):
    '''
    This function validates if it is possible to move the card in the tableau
    stack to another tableau stack, and returns if it is true or false.
    Parameters: tableau(list of lists),source pile(list),destination pile(list)
    returns: boolean(true or false)
    displays: none
    '''
    #pass    # replace this line with your code
    
    #if source or destination too big, return false
    if s > 17:
        print("Error in Source.")
        return False
    if d > 17:
        print("Error in Destination.")
        return False
    
    #if length of source is zero then return false
    if len(tableau[s]) == 0:
        print("Error in move: MTT , {} , {}".format(s,d))
        return False
    #if length of destination is zero then return false
    if len(tableau[d]) == 0:
        print("Error in move: MTT , {} , {}".format(s,d))
        return False
    
    #if length of destination is 3, then it's too big so return false
    if len(tableau[d]) == 3:
        print("Error in move: MTT , {} , {}".format(s,d))
        return False
    
    #getting ranks of source card and destination top card
    source_rank = tableau[s][-1].rank()
    
    dest_rank = tableau[d][-1].rank()
    
    #checks if within one, returns false if not
    if (source_rank + 1) != dest_rank and (source_rank - 1) != dest_rank:
        print("Error in move: MTT , {} , {}".format(s,d))
        return False
    
    return True
def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''
    This function validates if the move from tableau to foundation is a valid
    move.
    Parameters: tableau, foundation, source, destination
    returns: boolean(true or false)
    displays: none
    '''
    
    if s > 17:
        print("Error in Source.")
        return False
    
    if d > 3:
        print("Error in Destination.")
        return False
    
    if len(tableau[s]) == 0:
        print("Error in move: MTF , {} , {}".format(s,d))
        return False
    
    if len(foundation[d]) == 0:
        source_rank = tableau[s][-1].rank()
        if source_rank == 1:
            return True
        else:
            print("Error in move: MTF , {} , {}".format(s,d))
            return False
    
    source_rank = tableau[s][-1].rank()
    
    dest_rank = foundation[d][-1].rank()
    
    source_suit = tableau[s][-1].suit()
    
    dest_suit = foundation[d][-1].suit()
    
    if (source_rank - 1) != dest_rank:
        print("Error in move: MTF , {} , {}".format(s,d))
        return False
    
    if source_suit != dest_suit:
        print("Error in move: MTF , {} , {}".format(s,d))
        return False
    
    return True    
    
    
def move_tableau_to_tableau(tableau,s,d):
    '''
    This function moves the card in tableau to the other tableau. It calls the 
    corresponding validate function to check if move is valid.
    Parameters: tableau, source , foundation
    returns: boolean true or false
    '''
    #pass    # replace this line with your code
    
    if not valid_tableau_to_tableau(tableau,s,d):
        return False
    
    tableau[d].append(tableau[s][-1])
    tableau[s].pop()
    return True
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''    
    This function moves the card in tableau to the foundation. It calls the 
    corresponding validate function to check if move is valid.
    Parameters: tableau, source , foundation
    returns: boolean true or false '''
    
    if not valid_tableau_to_foundation(tableau,foundation,s,d):
        return False
    
    foundation[d].append(tableau[s][-1])
    tableau[s].pop()
    return True
def check_for_win(foundation):
    ''' Docstring '''
    
    for i in foundation:
        if len(i) != 13:
            return False
        
    return True

def undo(moves,tableau,foundation):
    '''
    Undo the last move;
       Parameters:
           moves: the history of all valid moves. It is a list of tuples 
                  (option,source,dest) for each valid move performed since the 
                  start of the game. 
           tableau: the data structure representing the tableau.  
       Returns: Bool (True if there are moves to undo. False if not)
    '''
       
    if moves: # there exist moves to undo
        last_move = moves.pop()
        option = last_move[0]
        source = last_move[1]
        dest = last_move[2]
        print("Undo:",option,source,dest)
        if option == 'MTT':
            tableau[source].append(tableau[dest].pop())
        else: # option == 'MTF'
            tableau[source].append(foundation[dest].pop())
        return True
    else:
        return False

def display(tableau, foundation):
    '''Display the foundation in one row;
       Display the tableau in 3 rows of 5 followed by one row of 3.
       Each tableau item is a 3-card pile separated with a vertical bar.'''
    print("\nFoundation:")
    print(" "*15,end='') # shift foundation toward center
    # display foundation with labels
    for i,L in enumerate(foundation):
        if len(L)==0:
            print("{:d}:    ".format(i),end="  ") # padding for empty foundation slot
        else:
            print("{:d}: {} ".format(i,L[-1]),end="  ") # display only "top" card
    print()
    print("="*80)
    print("Tableau:")
    # First fifteen 3-card piles are printed; across 3 rows
    for i in range(15):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:  # print 3-card pile (list)
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
        if i%5 == 4: # start a new line after printing five lists
            print()
            print("-"*80)
    # Final row of only three 3-card piles is printed
    print(" "*15+"|",end='')  # shift first pile right
    for i in range(15,18):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
    print()
    print("-"*80)
    


def main():  
    '''
    This is the main function of the program. It calls the other functions to 
    run the game of shamrocks, and will keep track of the game and whether the
    user wins or not
    Parameters: None
    returns: none
    '''
    
    print("\nWelcome to Shamrocks Solitaire.\n")\
    
    undo_list = []    
    
    tableau,foundation = initialize()
    display(tableau,foundation)
    print(MENU)
    
    while True:
        option_str = get_option()
        #print(get_option())
        
        if option_str == None:
            pass
        
        #Quits the program
        elif option_str == ["Q"]:
            break
        
        # elif option_str == None:
        #     print("Error in option: {}".format(option_str))
        
        elif option_str == ['U']:
            undo_res = undo(undo_list,tableau,foundation)
            if undo_res:
                #undo_list.pop()
                display(tableau,foundation)
            
        #displays menu of choices and reprompts for input
        elif option_str == ["H"]:
            print(MENU)
        
        #resets the game and displays the menu again
        elif option_str == ["R"]:
            tableau,foundation = initialize()
            print(MENU)
            
        elif len(option_str) == 3:
            if option_str[0].upper() == "MTT":
                res = move_tableau_to_tableau(tableau,option_str[1],option_str[2])
                
                if check_for_win(foundation):
                    print("You won!")
                    display(tableau,foundation)
                    print("\n- - - - New Game. - - - -")
                    tableau,foundation = initialize()
                    display(tableau,foundation)
                    print(MENU)
                
                elif res:
                    undo_list.append((option_str[0].upper(),option_str[1],option_str[2]))
                    display(tableau,foundation)
                
            elif option_str[0].upper() == "MTF":
                res = move_tableau_to_foundation(tableau,foundation,option_str[1],option_str[2])
                
                if check_for_win(foundation):
                    print("You won!")
                    display(tableau,foundation)
                    print("\n- - - - New Game. - - - -")
                    tableau,foundation = initialize()
                    display(tableau,foundation)
                    print(MENU)
                
                elif res:  
                    undo_list.append((option_str[0].upper(),option_str[1],option_str[2]))
                    display(tableau,foundation)
            
        #error check for valid option
        else:
            pass
        
        
                    
            
        
        
        
        
        
        
    print("Thank you for playing.")
        

if __name__ == '__main__':
     main()