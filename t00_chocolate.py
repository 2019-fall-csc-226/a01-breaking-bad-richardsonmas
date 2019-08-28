######################################################################
# Author: Scott Heggen & Emily Lovell           ****** TODO: CHANGE THIS!! ******
# username: heggens & lovelle             ****** TODO: CHANGE THIS!! *****
#
# Purpose: Designed to compute the total chocolate desired by the user
#
######################################################################
# Acknowledgements:
#
# Modified from original code written by Dr. Jan Pearce
#
# Licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################



# Section 1: User Input Section
print("")
entered_name = input("Please enter your name: ")
print("Hello " + entered_name + "! \n")

num_boxes = int(input("How many chocolate boxes you would like? "))
num_lbs = int(input("How many lbs of chocolate in a box? \n"))


# Section 2: Computation Section
lbs_choc = num_boxes * num_lbs
oz_per_lb = 16
oz_choc = lbs_choc * oz_per_lb


# Section 3: Conditional (Decision-making) Section
if oz_choc > 500:
    print("Wow, you must really like chocolate!")
else:
    print("Not a choc-o-holic, I guess! ")

# Section 4: Displaying Results Section
print(str(num_boxes) + " boxes\nwith " + str(num_lbs) + " lbs of chocolate per box\nis" + " " + str(oz_choc) + " ounces of chocolate.\n" )
print("Studies have shown there are health benefits from eating 1.5 to 3 ounces of dark chocolate daily!")

# To run this code, hit the green run button.
