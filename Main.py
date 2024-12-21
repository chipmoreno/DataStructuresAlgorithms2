## Christopher Moreno Student ID 010725508

import csv
import datetime
import Truck
from CreateHashTable import *
from Package import *

# Importing distances CSV

with open("DST.csv") as dist_file:
    CSV_Distance = list(csv.reader(dist_file))

# Importing Address CSV

with open("ADD.csv") as add_file:
    CSV_Address = list(csv.reader(add_file))

# Importing Package CSV

with open("PKG.csv") as pkgfile:
    CSV_Package = list(csv.reader(pkgfile))

# Defining function Load Package Data - putting package data into a list and then a hash map

def load_package_data(filename, PKGHASH):
        for package in csv.reader(open(filename)):
            ID = int(package[0])
            Address = package[1]
            City = package[2]
            State = package[3]
            Zipcode = package[4]
            Deadline_time = package[5]
            Weight = package[6]
            Status = "At Hub"
            p = Package(ID, Address, City, State, Zipcode, Deadline_time, Weight, Status)
            PKGHASH.insert(ID, p)

# Defining function Distance In Between - setting empty distance fields in distance CSV

def distance_in_between(x, y):
    distance = CSV_Distance[x][y]
    if distance == '':
        distance = CSV_Distance[y][x]

    return float(distance)

# Defining function Extract Address: 

def extract_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])

# Instantiating Truck objects

truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

truck2 = Truck.Truck(16, 18, None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# Creatinga  Hash Map

PKGHASH = CreateHashMap()

# Loading package data into Hashmap

load_package_data("PKG.csv", PKGHASH)

# DeliverPack: retrieves packages 
# clears package list, and 
# returns list retrieved packages

def deliverPack(truck):
    not_delivered = []
    for packageID in truck.packages:
        package = PKGHASH.lookup(packageID)
        not_delivered.append(package)
    truck.packages.clear()
        

# Implementation of Nearest Neighbor algorithm. finds the nearest undelivered package
#  to the truck's current address, adds it to the truck's delivery route, 
# updates the truck's mileage, address, and time, sets the package's delivery 
# and departure times, and removes it from the list of undelivered packages 
# until all packages are delivered.

    while len(not_delivered) > 0:
        NXTADD = 2000
        next_package = None
        for package in not_delivered:
            if distance_in_between(extract_address(truck.address), extract_address(package.address)) <= NXTADD:
                NXTADD = distance_in_between(extract_address(truck.address), extract_address(package.address))
                next_package = package
        truck.packages.append(next_package.ID)
        not_delivered.remove(next_package)
        truck.mileage += NXTADD
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=NXTADD / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time

deliverPack(truck1)
deliverPack(truck2)
truck3.depart_time = min(truck1.time, truck2.time)
deliverPack(truck3)

# Main Class, starts user interface

class Main:
    print("WGU PARCEL SERVICE (WGUPS)")
    print("ROUTE MILEAGE:")
    print(truck1.mileage + truck2.mileage + truck3.mileage)
    text = input("Type START: \n")
    if text == "START":
        try:
            user_time = input("ENTER TIME TO CHECK PACKAGE STATUS(ES). USE FORMAT HH:MM:SS: \n")
            (h, m, s) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            second_input = input("TO VIEW INDIVIDUAL PACKAGE STATUS TYPE SOLO, FOR ALL TYPE ALL \n")
            if second_input == "SOLO":
                try:
                    solo_input = input("ENTER PACKAGE ID \nS")
                    package = PKGHASH.lookup(int(solo_input))
                    package.UpdateStatus(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("INVALID, EXITING")
                    exit()
            elif second_input == "ALL":
                try:
                    for packageID in range(1, 41):
                        package = PKGHASH.lookup(packageID)
                        package.UpdateStatus(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("INVALID, EXITING")
                    exit()
                print("ROUTE MILEAGE:")
                print(truck1.mileage + truck2.mileage + truck3.mileage)
            else:   
                exit()
        except ValueError:
            print("INVALID, EXITING")
            exit()
    elif input != "START":
        print("INVALID, EXITING")
        exit()
