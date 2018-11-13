from vector import *


# Add two vectors
print('')
print('#### Add Two Vectors ####')
vector1 = Vector([1,2,3])
print vector1
vector2 = Vector([3,6,9])
print vector2
vectorSum = vector1.plus(vector2)
print vectorSum

# Subtract vector2 from vector1
print('')
print('#### Subrtract Two Vectors ####')
vectorDifference = vector1.minus(vector2)
print vectorDifference

# Multiply vector1 by a scaler
print('')
print('#### Multiply a Vector by a Scalar ####')
scaledVector = vector1.times_scalar(4)
print scaledVector

# Find the magnitude of vector2
print('')
print('#### Find the Magnitude of a Vector ####')
print (vector2.magnitude())

# Find the unit vector of vector2
print('')
print('#### Find the Unit Vector of a Vector ####')
print(vector2.normalized())

# compute the dot product of two vectors
print('')
print('#### Compute the Dot Product of Two Vectors ####')
vector1 = Vector([7.887,4.138])
vector2 = Vector([-8.802,6.776])
print (vector1.dot(vector2))

# compute the angle between two vectors in radians
print('')
print('#### Compute the Angle Between Two Vectors in Radians ####')
vector1 = Vector([5, 10])
vector2 = Vector([22.737, 23.64])
print(vector1.angle_with(vector2,False))

# compute the angle between two vectors in degrees
print('')
print('#### Compute the Angle Between Two Vectors in Degrees ####')
vector1 = Vector([7.35,0.221,5.188])
vector2 = Vector([2.751,8.259,3.985])
print(vector1.angle_with(vector2,True))

# check if two vectors are orthogonal or parallel
print('')
print('#### Check if two Vectors are Orthogonal or Parallel ####')
v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print 'is parallel:', v1.is_parallel_to(v2)
print 'is orthogonal:', v1.is_orthogonal_to(v2)
