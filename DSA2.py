import csv

# Open the CSV file and read it
with open('PackageCSV.csv', 'r') as pkgCSV:
    pkgData = csv.reader(pkgCSV, delimiter=',')
    data_read = [row for row in pkgData]  # Read all data into a list
    
# Initialize the packages dictionary
packages = {}

# Iterate through each row in the CSV data
for row in data_read:
    package_id = int(row[0])  # Convert ID to an integer
    address = row[1]
    city = row[2]
    state = row[3]
    zip_code = row[4]
    delivery_time = row[5]
    weight = row[6]
    notes = row[7]

    # Add the package data to the packages dictionary
    packages[package_id] = {
        "address": address,
        "city": city,
        "state": state,
        "zip": zip_code,
        "delivery_time": delivery_time,
        "weight": weight,
        "notes": notes
    }

# Print the resulting hash table (Packages)
print(packages)
