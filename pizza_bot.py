# Pizza Bot Program

import random
from random import randint

# List of random names
names = ["Luka", "kade", "Jayden", "Jason", "Max verstappen", "Michael Schumacher", "Rory", "Antonie", "Lucas", "Charles Leclerc"]

# Welcome message with random name

def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

# Menu for pickup or delivery






# Pick up information






# Delivery information - name address and phone





# Choose total number of pizzas - max 5






# Pizza menu 






# Pizza order - from menu - print each pizza ordered with cost





# Print order out - including if order is delivery or pickup and names and price of each pizza  - total cost including any delivery charge




# Ability to cancel or proceed with order





# Option for new order or to exit







# Main function

def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()


main()

