import math
import csv
from library_week6 import *

f= lambda x: x/(x+1)                    #function
analytical_result= 1.3068528194         #calculated manually

print("Actual Analytical Value=", analytical_result)
print()


print("Numerical Integration using Midpoint/Rectngle Method")
midpoint1 = midpoint (1,3,5,f)
midpoint2 = midpoint (1,3,10,f)
midpoint3 = midpoint (1,3,25,f)

print("Table of N, Numerical value and Difference with actual value")
print("N=5,    Ans=", midpoint1,",    Difference=", round(abs(midpoint1-analytical_result),10))
print("N=10,   Ans=", midpoint2,",   Difference=", round(abs(midpoint2-analytical_result),10))
print("N=25,   Ans=", midpoint3,",   Difference=", round(abs(midpoint3-analytical_result),10))
print()


print("Numerical Integration using Trapezoidal Method")
trapezoidal1 = trapezoidal (1,3,5,f)
trapezoidal2 = trapezoidal (1,3,10,f)
trapezoidal3 = trapezoidal (1,3,25,f)

print("Table of N, Numerical value and Difference with actual value")
print("N=5,    Ans=", trapezoidal1,",   Difference=", round(abs(trapezoidal1-analytical_result),10))
print("N=10,   Ans=", trapezoidal2,",   Difference=", round(abs(trapezoidal2-analytical_result),10))
print("N=25,   Ans=", trapezoidal3,",    Difference=", round(abs(trapezoidal3-analytical_result),10))
print()


print("Numerical Integration using Simpson Method")
simpson1 = simpson (1,3,6,f)
simpson2 = simpson (1,3,10,f)
simpson3 = simpson (1,3,26,f)

print("Table of N, Numerical value and Difference with actual value")
print("N=6,    Ans=", simpson1,",   Difference=", round(abs(simpson1-analytical_result),10))
print("N=10,   Ans=", simpson2,",   Difference=", round(abs(simpson2-analytical_result),10))
print("N=26,   Ans=", simpson3,",   Difference=", round(abs(simpson3-analytical_result),10))



#Appended Result
'''
Actual Analytical Value= 1.3068528194

Numerical Integration using Midpoint/Rectngle Method
Table of N, Numerical value and Difference with actual value
N=5,    Ans= 1.308092114284065 ,    Difference= 0.0012392949
N=10,   Ans= 1.3071646395900398 ,   Difference= 0.0003118202
N=25,   Ans= 1.3069028019555275 ,   Difference= 4.99826e-05

Numerical Integration using Trapezoidal Method
Table of N, Numerical value and Difference with actual value
N=5,    Ans= 1.3043650793650796 ,   Difference= 0.00248774
N=10,   Ans= 1.3062285968245722 ,   Difference= 0.0006242226
N=25,   Ans= 1.306752839424082 ,    Difference= 9.998e-05

Numerical Integration using Simpson Method
Table of N, Numerical value and Difference with actual value
N=6,    Ans= 1.3068302068302067 ,   Difference= 2.26126e-05
N=10,   Ans= 1.3068497693110697 ,   Difference= 3.0501e-06
N=26,   Ans= 1.3068527513069685 ,   Difference= 6.81e-08
'''
