import csv
csv_col=['ID','Name','Place']
dict_data=[{'ID':1,'Name':'Anu','Place':'Veettoor'},
{'ID':2,'Name':'Ajmal','Place':'Veettoor'},
{'ID':3,'Name':'Jeny','Place':'Veettoor'},
{'ID':4,'Name':'Afla','Place':'Veettoor'},
{'ID':5,'Name':'Thasni','Place':'Veettoor'},
{'ID':6,'Name':'Akhila','Place':'Veettoor'},
{'ID':7,'Name':'Anjaly','Place':'Veettoor'},
{'ID':8,'Name':'Jilta','Place':'Veettoor'},
{'ID':9,'Name':'Ameen','Place':'Veettoor'},
{'ID':10,'Name':'Mahendran','Place':'Veettoor'}]
try:
    with open ("Names.csv", 'w') as file1:
        #Writing CSV files using csv.writer()
        writer1 = csv.DictWriter (file1, fieldnames=csv_col)
        writer1.writeheader ()
        for data1 in dict_data:
            writer1.writerow(data1)
except IOError:
    print("I/O error")
data1 = csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data1:
   print(row)
