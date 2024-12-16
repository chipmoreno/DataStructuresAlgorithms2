import csv

with open('PackageCSV.csv', 'r') as pkgCSV:    
   pkgData = csv.reader(pkgCSV, delimiter=',')
   data_read = [row for row in pkgData]
   print(data_read)