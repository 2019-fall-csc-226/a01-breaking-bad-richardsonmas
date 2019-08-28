######################################################################
# Author: Scott Heggen & Emily Lovell
# Username: heggens & lovelle
#
# Assignment: A01 example
# Purpose: A class demonstration of if, elif, else, and nested if statements
######################################################################
# Acknowledgements:
#   This program utilizes inspiration for the timey wimey stuff
#   from Doctor Who: http://en.wikipedia.org/wiki/Doctor_Who and
#   quotes from http://www.brainyquote.com/quotes/topics/topic_computers.html

#   Original Author: Dr. Jan Pearce
######################################################################
import time          # import a library with time.sleep()
import random        # import a library with random.choice()

# This is how to ask for input from the keyboard:
my_input = input('Please enter a three letter word: ')

print('Your word is: ' + my_input + '!')

print('')                           # This prints a blank line.

if my_input == 'cat' or my_input == 'dog':
    # This print statement will only run if my_input is either 'cat' or 'dog'.
    print('I guess you like pets!')
    if my_input == 'dog':
        # This print statement will only run if my_input is 'dog'
        print('If a dog barks his head off in the forest and no human hears him, is he still a bad dog?')
    else:
        # These print statements will only run if my_input is 'cat'
        print('What do cats like to eat for breakfast?')
        time.sleep(2)
        print('Mice Krispies!')
elif my_input == 'the':
    # This print statement will only run if my_input is 'the'
    print('What the???')
elif my_input == 'and':
    # This print statement will only run if my_input is 'and'
    print('and, what???')
elif my_input == 'for':
    # This print statement will only run if my_input is 'for'
    print('What for???')
elif my_input == 'but':
    # This print statement will only run if my_input is 'but'
    print("but what?! Don't be contrary!")
else:
    # This print statement will only run if my_input is not any of the other options above
    print('Thanks for the ' + my_input + '!')

# The following quotes are from http://www.brainyquote.com/quotes/topics/topic_computers.html
saying1 = 'Computing is not about computers any more. It is about living...  N. Negroponte'
saying2 = 'Computers are famous for being able to do complicated things starting from simple programs... S. Lloyd'
saying3 = 'The good news about computers is that they do what you tell them to do. The bad news is that they do what you tell them to do... T. Nelson'
saying4 = 'The digital revolution is far more significant than the invention of writing or even of printing... D. Engelbart'
# The following is from http://en.wikipedia.org/wiki/Doctor_Who
saying5 = 'The world would be a poorer place without Doctor Who... Director Steven Spielberg'

some_choice = random.choice([saying1, saying2, saying3, saying4, saying5])

time.sleep(0.5)
print('')
print('Have you heard this one?')
print(some_choice)
