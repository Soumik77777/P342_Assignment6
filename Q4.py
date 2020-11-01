import math
import csv
from library_week6 import *

f=lambda x: 4/((x**2)+1)

list_N= []
list_value = []

for i in range (1, 4000):
    N= i*10
    montecarlo = monte_carlo (0,1,N,f)
    print("For N=",N,",    Integration value=", montecarlo)    #printing result for N=10, 20, 30... 40000
    list_N.append(N)
    list_value.append(montecarlo)

with open('Q4_montecarlo_datafile.csv', 'w', newline='') as file:       #creating csv file
    writer = csv.writer(file)
    writer.writerow(["N", "Integration Value"])
    for i in range (len(list_N)):
        writer.writerow([list_N[i], list_value[i]])                     #adding values in csv


'''
The output is of 4000 lines, so it's not appended. The attached CSV file contains all the result.
'''