#Thoran Landers and Janos Revesz 01/10/2019
#import sqrt function
from numpy import sqrt

#point is projected vertically at 10m/s from a 
# height of 15m above ground

#acceleration due to gravity
g = -9.81
#initial velocity
v0 = 10
#initial height
z0 = 15
#final height
z = 0.0

#calculate final speed using constant acceleration equations
v2 = v0**2 + 2*g*(z-z0)
speed = sqrt(v2)

#output whether positive or negative
#when positive point is projected upward
#when negative point is projected downwards
#when zero point is released from rest
if v0 > 0:
    print("v0 is positive")
else:
    print("v0 is less than or equal to zero")

#calculate time taken
time_taken = -(speed + v0)/g

#output values for final velocity and time taken
print("Final velocity =", speed, "m/s")
print("Time taken = ", time_taken, "m/s")
