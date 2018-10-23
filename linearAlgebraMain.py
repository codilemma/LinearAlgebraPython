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
