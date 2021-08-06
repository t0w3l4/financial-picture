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
    contr_made = content_list[2]
    curr_amt = content_list[3]
    total_withdr = content_list[4] + "\n"

    # Split up the contribbution line
    [room_txt, room_amt] = contr_room.split(':')
    [made_txt, made_amt] = contr_made.split(':')
    [total_txt, total_amt] = curr_amt.split(':')

    # Get the contribution amount then add it to the total
    contr_room_amt = room_amt[2::]
    contr_made_amt = made_amt[2::]
    tfsa_total_amt = total_amt[2::]

    no_comma_room = ''
    no_comma_contr = ''
    no_comma_total = ''

    contr_comma = 0
    room_comma = 0
    total_comma = 9

    # Store comma value to be added when converting to string
    for is_contr_comma in contr_room_amt:
        if is_contr_comma != ',':
            contr_comma += 1
        else:
            break

    for is_made_comma in contr_made_amt:
        if is_made_comma != ',':
            room_comma += 1
        else:
            break

    for is_total_comma in tfsa_total_amt:
        if is_total_comma != ',':
            total_comma += 1
        else:
            break

    # Get rid of any possible commas
    for room_letter in contr_room_amt:
        if room_letter != ',':
            no_comma_room += room_letter
        else:
            continue

    for contr_letter in contr_made_amt:
        if contr_letter != ',':
            no_comma_contr += contr_letter
        else:
            continue

    for total_letter in tfsa_total_amt:
        if total_letter != ',':
            no_comma_total += total_letter
        else:
            continue

            # Convert string to float
    new_contr_room = float(no_comma_room)
    new_made_amt = float(no_comma_contr)
    new_tfsa_total = float(no_comma_total)

    # "Add" contribution to account
    new_contr_room -= contr_amt
    new_made_amt += contr_amt
    new_tfsa_total += contr_amt

    # Add comma to number
    if new_contr_room >= 1000:
        str_contr_room = str(new_contr_room)[
            :contr_comma:] + ',' + str(new_contr_room)[contr_comma::]
    else:
        str_contr_room = str(new_contr_room)

    if new_made_amt >= 1000:
        str_made_amt = str(new_made_amt)[
            :room_comma:] + ',' + str(new_made_amt)[room_comma::]
    else:
        str_made_amt = str(new_made_amt)

    if new_tfsa_total >= 1000:
        str_tfsa_total = str(new_tfsa_total)[
            :total_comma:] + ',' + str(new_tfsa_total)[total_comma::]
    else:
        str_tfsa_total = str(new_tfsa_total)

    # Convert new contr room to strings and format it
    str_new_contr_room = room_txt + ": $" + str_contr_room + "\n"
    str_new_made_amt = made_txt + ": $" + str_made_amt + "\n"
    str_new_curr_total = total_txt + ": $" + str_tfsa_total + "\n"

    stats_file.close()

    # Update the file with new changes
    updated_file = open("Text files/test_tfsa_stats.txt", "w")

    # Create long string to be written
    new_info = total_contr + str_new_contr_room + \
        str_new_made_amt + str_new_curr_total + total_withdr
    updated_file.write(new_info)
    updated_file.close()


add_contr(100.01)


def withdraw(withdrawal_amount):
    return 0


def update_curr_amount(new_total):
    return 0
