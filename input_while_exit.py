"""
Program : input_while.py
Author : Olivia Kennedy
Date Last Modified : 06/12/2020
This program prompts the user for correct input in the range of 1 - 100. Only correct input is stored in
the list, which is printed once the sentinel value (-99 in this program) is entered
"""
#prompt for good input
user_list = []
user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to view the list of good input:"))


while user_input != -99:
    if 1 <= user_input and 100 >= user_input:
        user_list.append(user_input)
    user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to view the list of good input:"))

#for loop
for u in user_list:
    print(u)
