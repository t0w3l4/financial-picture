"""
Purpose: Keep track of TFSA contribution room.
Inputs:
Outputs:
Author: t0w3l4
Date: August 4, 2021
Last updated: August 4, 2021

References:

"""


def tfsa_picture():
    stats_file = open("Text files/test_tfsa_stats.txt", "r")
    content = stats_file.read()

    return content


#print(tfsa_picture())


def add_contr_room(contribution_increase):
    stats_file = open("Text files/test_tfsa_stats.txt", "w")
    content = stats_file.read()

    stats_file.close()

    return 0


def add_contr(contribution):
    contr_amt = contribution

    stats_file = open("Text files/test_tfsa_stats.txt", "r")
    content = stats_file.read()

    content_list = content.split("\n")

    if content_list[-1] == '':
        del content_list[-1]

    # Store the line that contains the contribution amount
    total_contr = content_list[0] + "\n"
    contr_room = content_list[1]
    curr_amt = content_list[2] + "\n"
    total_withdr = content_list[3] + "\n"

    # Split up the contribbution line
    [room_txt, room_amt] = contr_room.split(':')

    # Get the contribution amount then add it to the total
    contr_room_amt = room_amt[2::]

    # Convert string to float
    new_contr_room = float(contr_room_amt)

    # "Add" contribution to account
    new_contr_room -= contr_amt

    # Convert new contr room to strings and format it
    str_new_contr_room = room_txt + ": $" + str(new_contr_room) + "\n"
    stats_file.close()

    # Update the file with new changes
    updated_file = open("Text files/test_tfsa_stats.txt", "w")

    # Create long string to be written
    new_info = total_contr + str_new_contr_room + curr_amt + total_withdr
    updated_file.write(new_info)
    updated_file.close()
    return 0


def withdraw(withdrawal_amount):
    return 0
