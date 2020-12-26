import csv

with open('test.csv', mode='w', newline="") as f:
    write = csv.writer(f)

    heading = ['fName', 'lName', 'email']
    write.writerow(heading)

    data = [
        ['Divya', 'X', 'divya@gmail.com'],
        ['Mariya', 'X', 'mariya@gmail.com'],
        ['balaji', 'X', 'balaji@gmail.com']
    ]
    write.writerows(data)
