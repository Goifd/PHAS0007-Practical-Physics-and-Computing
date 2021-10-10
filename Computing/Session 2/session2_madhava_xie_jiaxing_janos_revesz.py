#Xie Jiaxing and Janos Revesz 08/10/2019
# The code below uses the Madhava apporximation to calculate pi/4 with an accuracy chosen by the user.
# Users can input the tolerance they want, the computer will display the results and compare it's accuracy
# to the pi from numpy library.
 
import numpy
pi = numpy.pi

# User input for desired tolerance
tolerance = input("Value for tolerance= ")
tolerance = float(tolerance)

# initializing variables
newterm = 1
value = 0
n = 0

# using while loop to calculate pi
while abs(newterm) > tolerance:
    newterm = (-1)**n/(2*n + 1)
    value += newterm
    #1e-5
    print("newterm= ",newterm)
    n += 1

# Displaying calculated values
print("The series is equal to: ",value," we calculated the first ",n-1, " terms")
print("Pi/4 according to numpy: ", pi/4)
print("numpy_PI-calculated_pi= ", pi/4 - value)


# Question 2
# Using a tolerance of 10^-n seems to give a difference
# between numpy's pi and the calculated pi of 4*10^-(n+1)
# for 0<n<7 based on this we can assume that this remains 
# true for n>7 and this proves that our result is accurate
# to n decimal places for a tolerance of 10^-n

# Question 3 
#Units used(Second)
# A: 4.525 * 10^11s
# B: 4.525 * 10^27s

#Question 4
# Based on multiple observation on multiple computers it
# is clear that the answer is dependent on which computer
# we use but the results are very similar if we focus on the results from one of them.
# Rather than measuring time we measured the number of calculations it took
# to get a value for a desired tolerance of n. The number of calculations for n is in the 
# form of 5*10^n. Assuming that each calculation takes roughly the same amount of time 
# we can extrapolate that the time it takes to calculate PI is in the form of a*10^n.
# Measuring this for n=5 and n=6 suggests the same. With 4.5s in the first case and 45.25s in the second case.
# Using this method we can come up with the time for n=16 and n=32:
#45.25*10^10s and 45.25*10^26s
#This method works well for the first few digits of pi but calculating more than 7 digits would take too much time,
# as time grows exponentially.