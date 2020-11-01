import math
import csv
from library_week6 import *


e= 2.718281828459045
f= lambda x: e**(-x**2)

max_error=0.001
max_d2f=2   #calculated manually
max_d4f=12   #calculated manually


print("Midpoint Method")
mp_N = midpoint_N (0,1,max_error,max_d2f)
midpoint= midpoint (0,1,mp_N,f)
print("For Maximum Error 0.001, N=", mp_N)
print("Value of Numerical Definite Integral using Midpoint Method =", midpoint)
print()

print("Trapezoidal Method")
trap_N = trap_N (0,1,max_error,max_d2f)
trapezoidal= trapezoidal (0,1,trap_N,f)
print("For Maximum Error 0.001, N=", trap_N)
print("Value of Numerical Definite Integration =", trapezoidal)
print()

print("Simpson Method")
simp_N = simp_N (0,1,max_error,max_d4f)
simpson= simpson (0,1,mp_N,f)
print("For Maximum Error 0.001, N=", simp_N)
print("Value of Numerical Definite Integration =", simpson)

'''
Midpoint Method
For Maximum Error 0.001, N= 10
Value of Numerical Definite Integral using Midpoint Method = 0.7471308777479975

Trapezoidal Method
For Maximum Error 0.001, N= 13
Value of Numerical Definite Integration = 0.7464612610366895

Simpson Method
For Maximum Error 0.001, N= 4
Value of Numerical Definite Integration = 0.7468249482544435
'''