from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # Can return the Vector coordinates by using "print my_vector" 
    # were my_vector = Vector([1,2,3])
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,v):
        # using the list comprehension method
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        # using a for loop
        #new_coordinates = []
        #n = len(self.coordinates)
        #for i in range(n):
        #   new_coordinates.append(self.coordinates[i] +v.coordinates[i])
        return Vector(new_coordinates)
    
    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    # Normalize a vector to find its unit vector which represents the direction.
    # u = (1/mag(v))*v
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    # Dot Product multiply two vectors V.W = ||V||*||w||*cos(theta)
    # theta is the angle between two vectors
    # V.W = v1*w1 + v2*w2 + .... + vn*wn
    # theta = arcos((V.W)/(mag(v)*mag(w)))
    # if dot product = 0, vectors are orthogonal
    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e

    # two vectors are are parallel if one is a scalar multiple of the other.
    # two vectors are orthogonal if their dot product is equal to zero.
    # if a vector is orthogonal to itself, it must be the zero vector.
    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self,v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)

    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance
