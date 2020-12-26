import csv

# with open('test.csv') as f:
#     data = csv.reader(f)
#     for row in data:
#         for column  in row:
#             print(column)
#         print("*"*20)

# with open('test.csv') as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row[0].ljust(10), row[1].ljust(10), row[2])

with open('test.csv') as f:
    data = csv.DictReader(f)       # k with v
    for i in data:
        print(i['fName'].ljust(10), i['lName'].ljust(10), i['email'])