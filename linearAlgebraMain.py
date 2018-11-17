from vector import *
from line import *

# Add two vectors
print('')
print('#### Add Two Vectors ####')
vector1 = Vector(['1','2','3'])
print vector1
vector2 = Vector(['3','6','9'])
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
vector1 = Vector(['7.887','4.138'])
vector2 = Vector(['-8.802','6.776'])
print (vector1.dot(vector2))

# compute the angle between two vectors in radians
print('')
print('#### Compute the Angle Between Two Vectors in Radians ####')
vector1 = Vector(['5', '10'])
vector2 = Vector(['22.737', '23.64'])
print(vector1.angle_with(vector2,False))

# compute the angle between two vectors in degrees
print('')
print('#### Compute the Angle Between Two Vectors in Degrees ####')
vector1 = Vector(['7.35','0.221','5.188'])
vector2 = Vector(['2.751','8.259','3.985'])
print(vector1.angle_with(vector2,True))

# check if two vectors are orthogonal or parallel
print('')
print('#### Check if two Vectors are Orthogonal or Parallel ####')
v1 = Vector(['-7.579', '-7.88'])
v2 = Vector(['22.737', '23.64'])
print 'is parallel:', v1.is_parallel_to(v2)
print 'is orthogonal:', v1.is_orthogonal_to(v2)

# Projection methods
print('')
print('#### Compute the parallel component of a vector with respect to the basis vector ####')
v = Vector(['3.039', '1.879'])
w = Vector(['0.825', '2.036'])
vpar = v.component_parallel_to(w)
print 'vpar = ', vpar

print('')
print('#### Compute the orthogonal component of a vector with respect to the basis vector ####')
vort = v.component_orthogonal_to(w)
print 'vort = ', vort

print('')
print('#### Check that the sum of the vpar and vort = v ####')
print 'v = vpar + vort = ', vpar.plus(vort)

# Find the cross product of two vectors
print('')
print('#### Find the Cross product of two vectors ####')
v1 = Vector(['8.462', '7.893', '-8.187'])
v2 = Vector(['6.984', '-5.975', '4.778'])
print 'V1xV2 = ', v1.cross(v2)

# Find the area of the parallelogram spanned by two vectors
print('')
print('#### Find the Area of the Parallelogram Spanned by Two Vectors ####')
v1 = Vector(['-8.987', '-9.838', '5.031'])
v2 = Vector(['-4.268', '-1.861', '-8.866'])
print 'area of parallelogram = ', v1.area_of_parallelogram_with(v2)

# Find the area of the triangle spanned by two vectors
print('')
print('#### Find the Area of the Triangle Spanned by Two Vectors ####')
v1 = Vector(['1.5', '9.547', '3.691'])
v2 = Vector(['-6.007', '0.124', '5.772'])
print 'area of triangle = ', v1.area_of_triangle_with(v2)

# Check to see if two lines are the same
print('')
print('#### Check to see if two lines are the same ####')
ell1 = Line(normal_vector=Vector(['4.046', '2.836']), constant_term = '1.21')
ell2 = Line(normal_vector=Vector(['10.115', '7.09']), constant_term = '3.025')
print 'intersection: ', ell1.intersection_with(ell2)

# Determine if the intersection of two lines
print('')
print('#### Determine if the intersection of two lines ####')
ell1 = Line(normal_vector=Vector(['7.204', '3.182']), constant_term = '8.68')
ell2 = Line(normal_vector=Vector(['8.172', '4.114']), constant_term = '9.883')
print 'intersection: ', ell1.intersection_with(ell2)

# Function will return "None" if the lines are parallel
print('')
print('#### Function will return "None" if the lines are parallel ####')
ell1 = Line(normal_vector=Vector(['1.182', '5.562']), constant_term = '8.68')
ell2 = Line(normal_vector=Vector(['1.773', '8.343']), constant_term = '9.525')
print 'intersection: ', ell1.intersection_with(ell2)