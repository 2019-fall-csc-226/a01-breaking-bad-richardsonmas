######################################################################
# Author: Mason Richardson      TODO: Change this to your name
# Username: richardsonmas         TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Class Objects Help: Corey Schafer https://www.youtube.com/watch?v=ZDa-Z5JzLYM&
#   Clear screen help: Senthil Kumaran and jesterjunk on Stack Overflow https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python

######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################

import time
import sys
import os

clear = lambda: os.system('cls')

# Here are the two classes, person and sign. This is where I keep information about the signs, and how I add to or check the people's attributes.
class Person:
    def __init__(self, birthyear, sign, name, best, worst):
        self.birthyear = birthyear
        self.sign = sign
        self.name = name
        self.best = best
        self.worst = worst


class Sign:
    def __init__(self, year, best, worst, name):
        self.year = year
        self.best = best
        self.worst = worst
        self.name = name


# There are only two people represented, the user and a friend.
user = Person("", "", "", "", "")
friend = Person("", "", "", "", "")

# Here are all the signs and the information including
# the most likely years, best matches, worst match, and it's actual name.
Rat = Sign(["1936", "1948", "1960", "1972", "1984", "1996", "2008"], ["Rat", "Dragon", "Monkey"], "Goat", " Rat")
Ox = Sign(["1937", "1949", "1961", "1973", "1985", "1997", "2009"], ["Ox", "Snake", "Rooster"], "Horse", "n Ox")
Tiger = Sign(["1938", "1950", "1962", "1974", "1986", "1998", "2010"], ["Tiger", "Horse", "Dog"], "Snake", " Tiger")
Rabbit = Sign(["1939", "1951", "1963", "1975", "1987", "1999", "2011"], ["Rabbit", "Goat", "Pig"], "Dragon", " Rabbit")
Dragon = Sign(["1940", "1952", "1964", "1976", "1988", "2000", "2012"], ["Dragon", "Monkey", "Rat"], "Rabbit",
              " Dragon")
Snake = Sign(["1941", "1953", "1965", "1977", "1989", "2001", "2013"], ["Snake", "Rooster", "Ox"], "Tiger", " Snake")
Horse = Sign(["1942", "1954", "1966", "1978", "1990", "2002", "2014"], ["Horse", "Dog", "Tiger"], "Ox", " Horse")
Goat = Sign(["1931", "1943", "1955", "1967", "1979", "1991", "2003", "2015"], ["Goat", "Pig", "Rabbit"], "Rat", " Goat")
Monkey = Sign(["1932", "1944", "1956", "1968", "1980", "1992", "2004"], ["Monkey", "Rat", "Dragon"], "Pig", " Monkey")
Rooster = Sign(["1933", "1945", "1957", "1969", "1981", "1993", "2005"], ["Rooster", "Ox", "Snake"], "Dog", " Rooster")
Dog = Sign(["1934", "1946", "1958", "1970", "1982", "1994", "2006"], ["Dog", "Tiger", "Horse"], "Rooster", " Dog")
Pig = Sign(["1935", "1947", "1959", "1971", "1983", "1995", "2007"], ["Pig", "Rabbit", "Goat"], "Monkey", " Pig")


# (Required) Task 1
# TODO Ask user for their birth year

# This function gets the information I need from the user about themselves.
def userinfocollector():
    user.name = input("What is your name?\n")
    clear()
    print("Hello " + user.name + ", welcome to the Chinese Zodiac Compatibility Test!!")
    time.sleep(1.2)
    user.birthyear = input("What year were you born? (Please give full year ex. 1993): \n")
    clear()
    print("...")
    time.sleep(0.5)
    print(user.birthyear)
    time.sleep(0.5)

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
# This function uses the provided information to look for connections in the list of animals, and changes
# things about the user instance based on that.
def findsign():
    if user.birthyear in Rat.year:
        print("You are a Rat! \n")
        user.sign = "Rat"
        user.best = Rat.best
        user.worst = Rat.worst
    elif user.birthyear in Ox.year:
        print("You are an Ox!")
        user.sign = "Ox"
        user.best = Ox.best
        user.worst = Ox.worst
    elif user.birthyear in Tiger.year:
        print("You are a Tiger!")
        user.sign = "Tiger"
        user.best = Tiger.best
        user.worst = Tiger.worst
    elif user.birthyear in Rabbit.year:
        print("You are a Rabbit!")
        user.sign = "Rabbit"
        user.best = Rabbit.best
        user.worst = Rabbit.worst
    elif user.birthyear in Dragon.year:
        print("You are a Dragon!")
        user.sign = "Dragon"
        user.best = Dragon.best
        user.worst = Dragon.worst
    elif user.birthyear in Snake.year:
        print("You are a Snake!")
        user.sign = "Snake"
        user.best = Snake.best
        user.worst = Snake.worst
    elif user.birthyear in Horse.year:
        print("You are a Horse!")
        user.sign = "Horse"
        user.best = Horse.best
        user.worst = Horse.worst
    elif user.birthyear in Goat.year:
        print("You are a Goat!")
        user.sign = "Goat"
        user.best = Goat.best
        user.worst = Goat.worst
    elif user.birthyear in Monkey.year:
        print("You are a Monkey!")
        user.sign = "Monkey"
        user.best = Monkey.best
        user.worst = Monkey.worst
    elif user.birthyear in Rooster.year:
        print("You are a Rooster!")
        user.sign = "Rooster"
        user.best = Rooster.best
        user.worst = Rooster.worst
    elif user.birthyear in Dog.year:
        print("You are a Dog!")
        user.sign = "Dog"
        user.best = Dog.best
        user.worst = Dog.worst
    elif user.birthyear in Pig.year:
        print("You are a Pig!")
        user.sign = "Pig"
        user.best = Pig.best
        user.worst = Pig.worst
    else:
        print("Sign not found")
    time.sleep(3)
    clear()

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year

#  Now the process starts over, but working on the friend instance instead.
def friendinfocollector():
    friend.name = input("What is your friend's name?\n")
    clear()
    friend.birthyear = input("What year was " + friend.name + " born? (Please give full year ex. 1993): \n")
    print("...")
    time.sleep(0.5)
    print(friend.birthyear)


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
def friendfindsign():
    if friend.birthyear in Rat.year:
        print(friend.name + " is a Rat! \n")
        friend.sign = "Rat"
        friend.best = Rat.best
        friend.worst = Rat.worst
    elif friend.birthyear in Ox.year:
        print(friend.name + " is an Ox! \n")
        friend.sign = "Ox"
        friend.best = Ox.best
        friend.worst = Ox.worst
    elif friend.birthyear in Tiger.year:
        print(friend.name + " is a Tiger! \n")
        friend.sign = "Tiger"
        friend.best = Tiger.best
        friend.worst = Tiger.worst
    elif friend.birthyear in Rabbit.year:
        print(friend.name + " is a Rabbit! \n")
        friend.sign = "Rabbit"
        friend.best = Rabbit.best
        friend.worst = Rabbit.worst
    elif friend.birthyear in Dragon.year:
        print(friend.name + " is a Dragon! \n")
        friend.sign = "Dragon"
        friend.best = Dragon.best
        friend.worst = Dragon.worst
    elif friend.birthyear in Snake.year:
        print(friend.name + " is a Snake! \n")
        friend.sign = "Snake"
        friend.best = Snake.best
        friend.worst = Snake.worst
    elif friend.birthyear in Horse.year:
        print(friend.name + " is a Horse! \n")
        friend.sign = "Horse"
        friend.best = Horse.best
        friend.worst = Horse.worst
    elif friend.birthyear in Goat.year:
        print(friend.name + " is a Goat! \n")
        friend.sign = "Goat"
        friend.best = Goat.best
        friend.worst = Goat.worst
    elif friend.birthyear in Monkey.year:
        print(friend.name + " is a Monkey! \n")
        friend.sign = "Monkey"
        friend.best = Monkey.best
        friend.worst = Monkey.worst
    elif friend.birthyear in Rooster.year:
        print(friend.name + " is a Rooster! \n")
        friend.sign = "Rooster"
        friend.best = Rooster.best
        friend.worst = Rooster.worst
    elif friend.birthyear in Dog.year:
        print(friend.name + " is a Dog! \n")
        friend.sign = "Dog"
        friend.best = Dog.best
        friend.worst = Dog.worst
    elif friend.birthyear in Pig.year:
        print(friend.name + " is a Pig! \n")
        friend.sign = "Pig"
        friend.best = Pig.best
        friend.worst = Pig.worst
    else:
        print("Sign not found")
    if user.sign == friend.sign:
        time.sleep(1)
        print("Hey, you two are the same sign!")
    else:
        pass
    time.sleep(3)
    clear()


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.

# This function compares the variables for best and worst matches between the user and the friend instance
# and responds accordingly to three possible outcomes, good match, bad match and everything else lol.
def compatibilitycheck():
    print("Now we will check your compatibility with " + friend.name + "!! \n")
    time.sleep(2.7)
    clear()
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print("...")
    clear()
    if user.sign in friend.best:
        print("The " + user.sign + " and the " + friend.sign + " are very compatible!! \n")
    elif user.sign == friend.worst:
        print("The " + user.sign + " and the " + friend.sign + " are not very compatible.. \nBut anyone can be friends! \n")
    else:
        print("Nothing in the stars suggests a good or bad connection between the " + user.sign + " and the " + friend.sign + ". \nYou are the deciders of your own fate! \n")
    time.sleep(20)

# TODO print if you are a strong match, no match, or in between

# There's probably a more proper way to do this, but I just ran all the above functions one right after another.
userinfocollector()
findsign()
friendinfocollector()
friendfindsign()
compatibilitycheck()
