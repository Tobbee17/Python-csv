import csv

with open('hrdata_modifed.csv') as db:
    reader = csv.reader(db)

    found = 0
    #success = 0

    employee = imput('Enter employee name:')

    for row in reader:
        if employee in row[0]:
            found = 1
            if row[4] == '99-999-9999':
                success = 1
    if found == 1:
        print('Employee found')
        if success == 1:
            print('Access Granted')
        else:
            print('Access denied')
    else:
        print('')
