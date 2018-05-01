#guestList.py

import csv

def main():

    with open("GuestList.txt", "r") as guestList:
        guests = csv.reader(guestList)

        for eachGuest in guests:
            print(eachGuest)
