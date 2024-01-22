##############################################################################
#   Computer Project #11
#       program that routes the best path between places using a graph!
#           ask for file input, greet the user
#           read user file
#           generate graph based on csv file
#           update graph with provided function
#           loop until user done
#               ask for a route with error checking with loop
#                   prevent duplicates and fake names and missing routes
#                   upon entering end
#                       give route and distance
#               upon entering 'q' for option 
#                   quits game and displays goodbye message
##############################################################################






import csv, place

def apsp(g):
    '''All-Pairs Shortest Paths using the Floyd-Warshall algorithm.'''
    '''DO NOT CHANGE'''

    INFINITE = 2**63-1  # a really big number (the biggest int for a 64-bit machine)

    # Initialize paths with paths for adjacent nodes
    paths = [[0 for j in range(len(g))] for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != 0: 
                paths[i][j] = [i,j] # if two places are already adjacent then assign an initial path to them
            elif i != j:  # i == j means this is the same place so distance is zero
                g[i][j] = INFINITE # replacing zero by an "infinite" value
                # zero earlier meant that two places are not connected, now it will mean that they are not connected
                # initially, meaning that are "very-very" far ("virtually", for the sake of initialization)


    #apsp computation - floyd-warshall algorithm
    for k in range(len(g)):  # (for each) vertex k, to compare if i--k + k--j is shorter than i--j computed so far
        for i in range(len(g)): # (for each) vertex i of our interest
            for j in range(len(g)): # (for each) vertex j, to get the computed distance so far (between i and j)
                if g[i][j] > g[i][k] + g[k][j]: # determining if there is a shorter path (as per the above comment)
                    g[i][j] = g[i][k] + g[k][j] # updating the path-length value if there is a shorter path

                    # updating the path itself if there is a shorter path
                    paths[i][j] = paths[i][k][:]
                    paths[i][j].extend(paths[k][j][1:])

    # if a pair of places are still at infinite distance,
    # then assign them 0, to declare that they are not connected 
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == INFINITE: 
                g[i][j] = 0

    return g,paths

def open_file():
    ''' 
    Asks the user to input a file to use, if not correct, reprompts user for 
    valid file input until correct
    
    Parameters: None
    return: fp (file pointer)
    displays: prompt and error message as appropriate
    '''
    file_str = input('Enter the file name: ')
    while True:
        try:
            fp = open(file_str, "r")
            return fp
            
        except FileNotFoundError:
            print('Invalid filename, please try again.')
            file_str = input('Input a file for reading: ')
            
def read_file(fp):
    '''
    Reads through the file line by line, and grabs the values for each index.
    Appends that to the list L. 
    Paramaters: fp (file pointer)
    return: L (list)
    '''
    #Initializing a list, read through file use csv reader
    L=[]
    reader = csv.reader(fp)
    next(reader,None)
    for line in reader:
        line[2] = int(line[2])
        tup = (line[0], line[1], line[2])
        
        L.append(tup)
    
    return L
        

def adjacency_matrix(L):
    '''
    Take places, add to the places list, remove duplicates and sort the list
    Size of matrix is dependant on the length of places in the list
    Create a matrix of a list of lists with 0's that is nxn length
    Puts each distance between places into the matrix
    Paramaters: L (list)
    return: places_lst (list), matrix (list(list))
    '''
    places_lst = []
    for line in L:
        places_lst.append(line[0])
        places_lst.append(line[1])
    places_lst = sorted(list(set(places_lst)))
    
    n = len(places_lst)
    
    matrix = []
    for i in range(n):
        lis = [0]*n
        matrix.append(lis)
        
    for line in L:
        first_index = places_lst.index(line[0])
        second_index = places_lst.index(line[1])
        
        third_index = line[2]
        
        matrix[first_index][second_index] = third_index
        matrix[second_index][first_index] = third_index
        
    return places_lst, matrix
    
def make_objects(places_lst,g):
    '''
    Call provided apsp function
    Initialize dictionaries for name and id
    Loop through names, make class, add to dictionary
    Paramaters: places_lst (list), g (list(list))
    return: indexed_by_name (dict), indexed_by_id (dict)
    '''
    g, paths = apsp(g)
    
    indexed_by_name = {}
    indexed_by_id = {}
    
    for idd, name in enumerate(places_lst):
        new_place = place.Place(name,idd)
        new_place.set_distances(g)
        new_place.set_paths(paths)
        
        indexed_by_name[name] = new_place
        indexed_by_id[idd] = new_place
    
    return indexed_by_name, indexed_by_id

def main():
    BANNER = '\nBegin the search!'
    
    #Call functions made above
    fp = open_file()
    L = read_file(fp)
    places_lst, matrix = adjacency_matrix(L)
    dic1, dic2 = make_objects(places_lst, matrix)
    
    #Last starting value was bad so don't print banner
    last = True
    
    while True:
        #Print banner
        if last:
            print(BANNER)
        last = True
        
        starting = input("Enter starting place, enter 'q' to quit: ")
        
        #Quit
        if starting.lower() == "q":
            break
        
        if starting not in places_lst:
            print('This place is not in the list!')
            last = False
            continue
        
        routes_list = [starting]
        
        #Get all the stops along the way, throws error if incorrect
        while True:
            next_input = input('Enter next destination, enter "end" to exit: ')
            if next_input.lower() == "end":
                break
            
            if next_input not in places_lst or next_input == routes_list[-1]:
                print('This destination is not valid or is the same as the previous destination!')
                continue
            
            routes_list.append(next_input)
        
        path_list = []
        distance = 0
        
        #Valid route or not
        failed = False
        
        #Go through routes
        for route in range(len(routes_list) - 1):
            destination = dic1[routes_list[route+1]].get_index()
            local_path = dic1[routes_list[route]].get_path(destination)
            local_distance = dic1[routes_list[route]].get_distance(destination)
            
            #Not a valid path
            if local_distance == 0:
                print('places {} and {} are not connected.'.format(routes_list[route],routes_list[route+1]))
                failed = True
            path_list.append(local_path)
            distance += local_distance
            
        if failed:
            continue
            
        print("Your route is:")
        
        #Print route
        for i in path_list:
            for j in i[:-1]:
                print("     {}".format(places_lst[j]))
        print("     {}".format(routes_list[-1]))
        print("Total distance = " + str(distance))
        
    print('Thanks for using the software')
    
if __name__=='__main__':
    main()
