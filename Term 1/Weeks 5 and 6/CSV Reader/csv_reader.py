import csv

with open('SalesRecords.csv', 'r') as open_file:
    csv_reader = csv.DictReader(open_file)
    print(type(csv_reader))
    for row in csv_reader:
        print(f"The profit for {row['Country']} and region {row['Region']} has been {float(row['Units Sold']) * float(row['Unit Price']) - float(row['Units Sold']) * float(row['Unit Cost'])}")
