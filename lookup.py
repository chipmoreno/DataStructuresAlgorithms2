import csv

# Reading the CSV file into a dictionary of packages
with open('PackageCSV.csv', 'r') as pkgCSV:
    pkgData = csv.reader(pkgCSV, delimiter=',')
    data_read = [row for row in pkgData]  # Read all data into a list

packages = {}

# Storing package details into a dictionary with package_id as the key
for row in data_read[1:]:  # Skipping the header row
    package_id = int(row[0])
    address = row[1]
    city = row[2]
    state = row[3]
    zip_code = row[4]
    delivery_time = row[5]
    weight = row[6]
    notes = row[7]

    packages[package_id] = {
        "address": address,
        "city": city,
        "state": state,
        "zip": zip_code,
        "delivery_time": delivery_time,
        "weight": weight,
        "notes": notes
    }

# Lookup function to find and return package details
def lookup_package(package_id):
    # Check if the package_id exists in the dictionary
    if package_id in packages:
        package = packages[package_id]
        return {
            "address": package["address"],
            "deadline": package["delivery_time"],  # Assuming delivery_time as deadline
            "city": package["city"],
            "zip_code": package["zip"],
            "weight": package["weight"],
            "status": "At the hub",  # Default status, as you didn't include a status in the data
            "delivery_time": package["delivery_time"]
        }
    else:
        return f"Package ID {package_id} not found."

# Test the lookup function with Package ID 1
print(lookup_package(1))
