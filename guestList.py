#guestList.py

import csv #import the csv module into the program

def main():

    with open("GuestList.txt", "r") as guestList: #opens GuestList.txt file, saves it as guestList, then closes the file
        guests = csv.reader(guestList) #goes through the entire guestList and seperates each entry with a comma
                                       #each line is its separate list entry

        for eachGuest in guests: #iterates through each entry in the "guests" list
            print(eachGuest) #prints out each entry in the "guests" list
