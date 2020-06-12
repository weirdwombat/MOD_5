"""
Program : input_while.py
Author : Olivia Kennedy
Date Last Modified : 06/12/2020
This program prompts the user for correct input in the range of 1 - 100. Only correct input is stored in
the list, which is printed once the sentinel value (-99 in this program) is entered.
"""
user_list = []
#prompt for good input
user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to stop:"))

while user_input != -99:
    while 1 > user_input or 100 < user_input:
        #prompt for bad input
        user_input = int(input("Please enter numbers from 1 to 100 only or enter -99 to stop:"))
    user_list.append(user_input)
    user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to stop:"))

#for loop
for u in user_list:
    print(u)


# observed outcome

# output for user input of 1 is the prompt for good input
# output for user input of 2 is the prompt for good input
# output for user input of 3 is the prompt for good input
# output for user input of -4 is the prompt given if the user gives bad input
# output for user input of 99 is the prompt given for good input
# output for user input of -99 is to print the list of the good input using a for loop
# the list printed after user input(that took place in the following order) of 1,2,3,-4,99,-99 is...
# 1
# 2
# 3
# 99
