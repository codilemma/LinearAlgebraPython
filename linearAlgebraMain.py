#import vector as my_vector
from vector import *


# Add two vectors
vector1 = Vector([1,2,3])
print vector1
vector2 = Vector([3,6,9])
print vector2
vectorSum = vector1.plus(vector2)
print vectorSum

# Subtract vector2 from vector1
vectorDifference = vector1.minus(vector2)
print vectorDifference

# Multiply vector1 by a scaler
scaledVector = vector1.times_scalar(4)
print scaledVector

# Find the magnitude of vector2
print (vector2.magnitude())

# Find the unit vector of vector2
print(vector2.normalized())

# compute the dot product of two vectors
vector1 = Vector([7.887,4.138])
vector2 = Vector([-8.802,6.776])
print (vector1.dot(vector2))

# compute the angle between two vectors in radians
vector1 = Vector([3.183, -7.627])
vector2 = Vector([-2.668,5.319])
print(vector1.angle_with(vector2,False))

#compute the angel between two vectors in degrees
vector1 = Vector([7.35,0.221,5.188])
vector2 = Vector([2.751,8.259,3.985])
print(vector1.angle_with(vector2,True))