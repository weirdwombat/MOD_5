user_list = []
#prompt for good input
user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to view the list of good input:"))


while user_input != -99:
    if 1 <= user_input and 100 >= user_input:
        user_list.append(user_input)
        user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to view the list of good input:"))
        if 1 > user_input or 100 < user_input:
            break
    user_input = int(input("Enter any number from 1 to 100, otherwise, enter -99 to view the list of good input:"))

#for loop
for u in user_list:
    print(u)
