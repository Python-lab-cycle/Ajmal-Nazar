import csv
with open('Employee1.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("Emp No. Emp Name")
    print("----------------")
    for i in data:
        print(i['Emp No.'],i['Emp Name'])
