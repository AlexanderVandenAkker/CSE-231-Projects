##############################################################################
#   Computer Project #1
#   Helpful Unit Conversions for Canoe Trip
#       prompted for a distance in rods
#       input a distance in rods
#       convert distance in rods to other units given
#       output the units converted from rods and time to walk
#   display rods, other conversions and the time to walk
##############################################################################

rod_str = input("Input rods: ") # enter distance in rods
rod_flt = float(rod_str) # converted input to a floating number
print("You input" , rod_flt, "rods.")

# define our variables and conversion operations
#the numbers given are defined constants for conversions from proj description 
r = (rod_flt) # number of rods
m = (r*5.0292) # distance in meters, converted from rods
ft = (m/0.3048) # distance in feet, converted from meters
mi = (m/1609.34) # distance in miles, converted from meters
fl= (r/40) # distance in furlongs, converted from rods

t = ((3.1*1609.34)/(60*5.0292)) #first conversion from miles/hour to rods/min
t = (1/t)# take the inverse of the previous answer to get mins/rod
t = t*r # mins to walk inputed value of rods

# display and round our outputed values from the input of rods

print("Conversions")
print("Meters:", round(m,3))
print("Feet:", round(ft,3))
print("Miles:", round(mi,3))
print("Furlongs:", round(fl,3))
print("Minutes to walk", r ,"rods:", round(t,3))