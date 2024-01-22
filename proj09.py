##############################################################################
#   Computer Project #9
#       program that reads a pokemon csv file and creates pokedex!
#           prompts the user for a proper csv file, error if not valid
#           displays options menu for user
#           prompts user for option about info from the pokedex(dictionary)
#               option 1 user is prompted to enter a pokemon name 
#                   then finds the pokemon and displays its info, reprompts to 
#                   continue with new option
#               option 2 user is prompted for abilities then finds and 
#                   displays all pokemon that have the abilities,reprompts to 
#                   continue with new option
#               option 3 user is prompted to enter a pokemon name, then 
#                   prompts user for matchup-type to pokemon, then finds and 
#                   displays all the pokemon with that type of matchup-type, 
#                   reprompts to continue with new option
#           an entry for option as 'q' or 'Q' will exit the program
##############################################################################               


import csv,copy

NAMES = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fight', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal',
'poison', 'psychic', 'rock', 'steel', 'water']
EFFECTIVENESS = {0.25: "super effective", 0.5: "effective", 1:"normal", 2:"weak", 4:"super weak", 0:"resistant"}
MATCHUP_TYPES = {"resistant", "super effective", "effective", "normal",
                 "weak", "super weak"}
PROMPT = '''
\nTo make a selection, please enter an option 1-3:\n
\tOPTION 1: Find Pokemon
\tOPTION 2: Find Pokemon From Abilities
\tOPTION 3: Find Matchups
\nEnter an option: '''

def open_file(s):
    """
     Asks the user to input a file to use, if not correct, reprompts user for 
    valid file input until correct
    
    Parameters: string(pokemon, to customize prompts)
    return: file_pointer
    displays: prompt and error message as appropriate
    """
    #prompts the user to enter file name, string s is formatted in it
    file_str = input("Please enter a {} filename: ".format(s))
    while True:
         #opens the file and reads all characters using "encoding='utf-8'"
         #returns a file pointer(opened file)
         try:
            fp = open(file_str, "r",encoding="utf-8")
            return fp
        
         #displays error message and reprompts user for file input   
         except FileNotFoundError:
            print("This {} file does not exist. Please try again.".format(s))
            file_str = input("Please enter a {} filename: ".format(s))

def read_file(fp):
    """
    This function takes in file pointer and reads through the csv file given,
    skips the first line then reads line by line and sorts the wanted info
    as well as assigns them values. It then organizes them into their needed
    object types. They are then added to a master dictionary with all the 
    information added to it.
    Parameters: file pointer (pokemon file)
    returns: dictionary(pokedex)
    displays: none
    """
    
    #initialize a dictionary and skip line in file
    D={}
    reader = csv.reader(fp)
    next(reader,None)
    
    for line in reader:
        #getting all variables
        generation = int(line[39])
        
        type1 = line[36]
        type2 = line[37]
        
        #handles missing types
        if type2 == "":
            type2= None
        type_tup = (type1,type2)
        
        capture_rate = int(line[23])
        hp = int(line[28])
        name = line[30]
        speed = int(line[35])
        weight = float(line[38])
        
        #determining if legendary
        legendary = False
        if line[40] == '1':
            legendary = True
        #cleaning up abilities list
        abil = line[0].replace("'","")[1:-1]
        abil = abil.split(",")
        for i in range(len(abil)):
            abil[i] = abil[i].strip()
            
        abil = set(abil)
        #get every matchup type
        against_dict = {}
        for i in MATCHUP_TYPES:
            against_dict[i]= set()
        for i in range(1,19):
            
            category = EFFECTIVENESS[float(line[i])]
            
            
            against_dict[category].add(NAMES[i-1])
                
            
                
        
        new_list = [against_dict,abil,hp,capture_rate,weight,speed,legendary]
        
        #generation is missing, so make every dict
        if generation not in D:
            name_dict = {}
            name_dict[name] = new_list
            types_dict = {}
            types_dict[type_tup] = name_dict
            D[generation] = types_dict
        #type tup is missing, so make one dict    
        elif type_tup not in D[generation]:
            name_dict = {}
            name_dict[name] = new_list
            D[generation][type_tup] = name_dict
        #everything execpt for name is there, creates new namekey and value    
        else:
            D[generation][type_tup][name]= new_list
            
        
    return D
    


def find_pokemon(pokedex, names):
    """
    This function iterates through the dictionary we created(pokedex) and 
    searches for specific info for those pokemon, based on the user input for
    pokemon in the main function. It then adds these to a list under the 
    pokemon name and then adds this to the dictionary(new_dict) that we
    created and returns that dictionary at the end.
    Paramaters: dict(pokedex), set of names given to search for
    returns: dictionary with pokemon name as key and lists of info as the value
    """
    
    #start by saving a deepcopy of the pokedex(dict) and init new_dict
    D = copy.deepcopy(pokedex)
    new_dict = {}
    #iterate through pokedex to find our info
    for generation in D:
        
        for typ in D[generation]:
            
            for name in D[generation][typ]:
                
                for n in names:
                    if name == n:
                        pokemon = D[generation][typ][name][1:]
                        pokemon.append(generation)
                        pokemon.append(typ)
                        new_dict[name] = pokemon
                        
    return new_dict
    
def display_pokemon(name, info):
    """
    This function takes in a name of a pokemon and the information about said
    pokemon, which is a key/value pair. This function then creates a string
    for the pokemon and it's info, and formats it to the appropriate printed
    format that we want.
    Parameters: string of pokemon name, and list of info for that pokemon
    returns: string, formatted the way we did in the functions.
    """
    
    #init an empty string and begins to build our info into it
    returnString = ""
    returnString += "\n" + name
    
    returnString += "\n\tGen: "  + str(info[6]) #generation
    
    #checks if there's two types or not and builds accordingly
    try:
        returnString += "\n\tTypes: " + info[7][0] + ", " + info[7][1]
        
    except TypeError:
        returnString += "\n\tTypes: " + info[7][0]
    #creates empty list for abilities so we can sort it
    abil_list = []
    for value in info[0]:
        abil_list.append(value)
    #sorts the list to alph order    
    abil_list.sort()
    returnString += "\n\tAbilities: "
    for i in range(len(abil_list) ):
        returnString += abil_list[i]
        if (i != len(abil_list) - 1):
            returnString += ", "
    #adds more values to our string    
    returnString += "\n\tHP: " + str(info[1])
    
    returnString += "\n\tCapture Rate: " + str(info[2])
    
    returnString += "\n\tWeight: " + str(info[3])
    
    returnString += "\n\tSpeed: "  + str(info[4])
    #adds legendary status to string based on the info for that index
    if info[5] == True:
        returnString += "\n\tLegendary"
    elif info[5] == False:
        returnString += "\n\tNot Legendary"
    #returns our completed strings
    return returnString

def find_pokemon_from_abilities(pokedex, abilities):
    """
    This function takes in a set of abilities and finds all pokemon that has 
    all of those specified abilities and then returns the set of pokemon 
    names with that set of abilities.
    Parameters: entire pokedex(dict) and set of abilities being looked for
    returns: set of all the names of pokemon who have all said abilities
    """
    
    #init an empty set for names
    names = set()
    
    #iterates through the pokedex to find their abilities, and checks if it's 
    #abilities given are a subset of abilities from the pokemon, adds to set
    for generation in pokedex:
        
        for typ in pokedex[generation]:
            
            for name in pokedex[generation][typ]:
                
                if abilities.issubset(pokedex[generation][typ][name][1]):
                    names.add(name)
    
    #returns the set of names that has the abilities 
    return names
                    
def find_matchups(pokedex, name, matchup_type):
    """
    This function takes in a pokemon's name and it's type effectiveness.
    It then takes the matchup type given, then finds the pokemon that 
    correspond with that matchup type to the original pokemon. It then returns
    the pokemon with that, and gives it's corresponding type(s) as well.
    Parameters: entire pokedex(dict), name of pokemon searching on(str) and 
    string with type effectivness we want to use
    returns: list of tuples with first index being name and second being a 
    tuple of their types
    """
    
    #initialize a list for matchups and dict for effective
    matchups = []
    effective = {}
    
    #iterates through the dict to find the pokemon name and types
    for generation in pokedex:
        
        for typ in pokedex[generation]:
            
            for nam in pokedex[generation][typ]:
                
                if name == nam:
                    effective = pokedex[generation][typ][name][0]
    #return none for improper matchup type                
    if not matchup_type in effective:
        return None
    #sets effective set to the key of the effective's matchup types
    effective_set = effective[matchup_type]
    
    #iterates through pokedex and finds pokemon with requested matchup type
    #then adds the pokemon with its matchup type effectiveness
    for generation in pokedex:
        
        for typ in pokedex[generation]:
            
            if typ[0] in effective_set or typ[1] in effective_set:
                
            
                for nam in pokedex[generation][typ]:
                    
                    if typ[1] == None:
                        matchups.append((nam,(typ[0],)))
                    
                    else:
                        matchups.append((nam,(typ[0],typ[1])))
                        
    #sorts the list of the pokemon given in alph order
    matchups.sort()
    return matchups
                    

def main():
    print("Welcome to your personal Pokedex!\n")
    fp = open_file("pokemon")
    pokedex = read_file(fp)
    
    #starts loop for main program
    while True:
        option_str = input(PROMPT)
        
        #inputing option as 'q' or 'Q' ends program
        if option_str.lower() == 'q':
            break
        
        #finds pokemon and abilities
        elif option_str == '1':
            pokemon_name = input("\nEnter a list of pokemon names, separated by commas: ")
            pokemon_list = pokemon_name.split(",")
            for i in range(len(pokemon_list)):
                pokemon_list[i] = pokemon_list[i].strip()
                
            pokemon_set = set(pokemon_list)
            pokemon_dict = find_pokemon(pokedex, pokemon_set)
            name_list = []
            for name in pokemon_dict:
                name_list.append(name)
            name_list.sort()
            for name in name_list:
                
                pokemon_dis = display_pokemon(name, pokemon_dict[name])
                print(pokemon_dis)
                
        #finds pokemon that have all said abilities    
        elif option_str == '2':
            pokemon_abil = input("Enter a list of abilities, separated by commas: ")
            abil_list = pokemon_abil.split(",")
            for i in range(len(abil_list)):
                abil_list[i] = abil_list[i].strip()
                
            abil_set = find_pokemon_from_abilities(pokedex, set(abil_list))
            abil_sorted = list(abil_set)
            abil_sorted.sort()
            print("Pokemon: ", end = '')
            for i in range(len(abil_sorted)):
                print(abil_sorted[i],end='')
                if i+1 < len(abil_sorted):
                    print(", ",end='')
            print()
                
            
            
        #finds all pokemon with matchup type for given pokemon     
        elif option_str == '3':
            poke_name = input("Enter a pokemon name: ")
            match_typ = input('Enter a matchup type: ')
            matchups = find_matchups(pokedex, poke_name, match_typ)
            
            if matchups == None:
                print("Invalid input")
            else:
                
                for i in matchups:
                    
                    print(i[0] + ': ', end ='')
                    if len(i[1]) > 1:
                        print(i[1][0] + ", " + i[1][1])
                        
                    else:
                        print(i[1][0])
                        
        #invalid input check and reprompts
        else:
            print("Invalid option {}".format(option_str))
            
            
    
    
    
    

if __name__ == "__main__":
    main()