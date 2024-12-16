import csv
from hashtable import HashFunction

class Package:
    def __init__(self, id, dest, weight, city, state, zip, deadline, notes, status):
        self.id = id
        self.dest = dest
        self.weight = weight
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.destination, self.city, self.state, self.Zip, self.deadline, self.mass, self.notes, self.status)

def loadData(csv):
    with open('PackageCSV.csv', 'r') as pkgCSV:
        pkgData = csv.reader(pkgCSV, delimiter=',')    
        for row in pkgData:
            id = int(row[0])
            dest = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery_time = row[5]
            weight = row[6]
            notes = row[7]
            status = "on board"
            newPack = Package(id, dest, city, state, zip, delivery_time, weight, notes, status)
            HashFunction.insert(id, newPack)

pkgHash = HashFunction()