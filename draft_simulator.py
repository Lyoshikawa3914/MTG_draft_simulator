# This program simulates a Magic the Gathering draft, with one pack
# Only pack 1 pick 1 are used
# REFER TO CH. 8.5 ABOUT PROBLEMS WITH MODIFYING A LIST WITH LOOPS

import sqlite3
import random

# The database is put into a variable
db_common = sqlite3.connect('mtg_common_war.db')

# Creates 8 lists representing booster packs
n = 8
packs = [[] for _ in range(n)]
count = 0
supercount = 10
deck = []

# function to rename sql table
def rename_table():
    c = db_common.cursor()
    c.execute("""DELETE FROM war_of_spark_commons WHERE id=1""")
    c.close()
#rename_table()

# Function will first create 8 lists representing packs
# The function will also randomly selects up to 10 names from the column Name

def random_selection(packs):
    count = 1
    c = db_common.cursor()

    # This will put 10 card names into each booster pack
    for pack in packs:
        c.execute("""Select NAME FROM war_of_spark_commons ORDER BY RANDOM() LIMIT 10""")
        row = c.fetchall()
        # This removes the the '[,]' from each string
        row = [i[0] for i in row]
        # print(row, '\n')
        for pos, card in enumerate(row):
            pack.append(row[pos])
        # print(pack)
        # print()
        # bot_card_selection(pack)
    c.close()
    return packs

# random_selection(packs)

# This function allows the player to choose a card from the pack and add it to their deck
def user_card_selection(pack, count):
    print("These are the cards in the pack")
    print("----------------------------------------------------------------------------------------------------------")
    print(pack)
    print()
    choice = input("Which card would you like to select? \n")
    # for card in pack:

    while count == 0:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])) or (choice == (pack[5])) or (choice == (pack[6])) or (choice == (pack[7])) or (
                choice == (pack[8])) or (choice == (pack[9])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 1:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])) or (choice == (pack[5])) or (choice == (pack[6])) or (choice == (pack[7])) or (
                choice == (pack[8])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 2:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])) or (choice == (pack[5])) or (choice == (pack[6])) or (choice == (pack[7])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 3:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])) or (choice == (pack[5])) or (choice == (pack[6])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 4:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])) or (choice == (pack[5])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 5:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])) or (
                choice == (pack[4])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 6:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])) or (choice == (pack[3])):
            # if choice == card:
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 7:
        if (choice == (pack[0])) or (choice == (pack[1])) or (choice == (pack[2])):
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    while count == 8:
        if (choice == (pack[0])) or (choice == (pack[1])):
            deck.append(choice)
            pack.remove(choice)
            break
        else:
            print("Sorry that is not a card in the pack. Please type again")
            print()
            choice = input("Which card would you like to select?")

    return


# Function allows the program to get a rating, based on the card name
def python_str_to_rating(names):
    rating = 0

    # May have to make a function for opp_pick
    opp_pick = []

    c = db_common.cursor()
    for name in names:
        c.execute("""Select RATING FROM war_of_spark_commons WHERE NAME = ?""", (name,))
        row = c.fetchall()
        row = [i[0] for i in row]
        integer = row[0]
        if (float(integer) > rating):
            rating = float(integer)
            opp_pick.append(name)
            names.remove(name)

            print()
    # This loop will reduce the number of items in opp_pick down to one item
    while len(opp_pick) > 1:
        for name in opp_pick:
            c.execute("""Select RATING FROM war_of_spark_commons WHERE NAME = ?""", (name,))
            row = c.fetchall()
            row = [i[0] for i in row]
            integer = row[0]  # this will assign the value to integer without [] or ''
            if (float(integer) < rating):
                opp_pick.remove(name)
                names.append(name)

    # print("The bots rating of the card is", rating)
    # print(opp_pick)
    # print(names)
    db_common.commit()
    c.close()
    return names


print("Welcome to the Magic the Gathering draft simulator")
print()
print("Please select a card from the pack")

random_selection(packs)
print()
# print(packs, '\n')
print()

for pos, i in enumerate(packs[:]):
    print("This is pack", pos + 1)
    user_card_selection(packs[:][pos], pos)
    print("This is your deck so far:")
    print("----------------------------------------------------------------------------------------------------------")
    print(deck)
    print("----------------------------------------------------------------------------------------------------------")
    count += 1
    if count < 8:
        for i in range(count):
            python_str_to_rating(packs[count])
            print()

print("Your deck is ready to go!")