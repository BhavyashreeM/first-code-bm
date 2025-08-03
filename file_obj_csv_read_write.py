#file =  open('test1.csv','w') # To create a new csv file in the path
"""
import csv  #module to work with csv files

data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]
#to write data into the csv file
with open('test1.csv','w',newline='') as file:
    wd = csv.writer(file) #.writer() method to create a CSV writer object, and then use its methods to write rows to the file.

    wd.writerows(data_to_write) #.writerows() method can parse something iterable (like a list of lists!) and write it into the CSV file


#to read data from the csv file
with open('test1.csv','r',encoding='utf8') as fr: #encoding="utf8" when opening the file. It helps Python properly read characters from the file.
    rf = csv.reader(fr) #.reader() method returns a list of rows where each row is a list of CSV data.

    for row in rf:
        print(row)





#Exercise -1


import csv

max_sales = 0
best_sell = None

with open('C:\\Users\\Bhavyadivya\\Documents\\Data Science_2025 materials\\Bestseller.csv','r',encoding='utf8') as fr:
  rf = csv.reader(fr) #, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
  # Skip the header row
  fr.readline()
  for row in rf:
      cur_sales = float(row[4])
      if cur_sales > max_sales:
         max_sales = cur_sales
         best_sell = row

  print('Best Selling Book row = ',best_sell)

"""
#Exercise -2

import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

with open('packing.csv','w',newline='') as wf:
  fw = csv.writer(wf)
  fw.writerows(data)

file_name = 'packing123.csv'

try:

  with open(file_name,'r',encoding='utf8') as rf:
    f_read = csv.reader(rf)
    for row in f_read:
     print(row)
except:
  print('Filenot Found')

