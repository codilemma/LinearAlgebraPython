import math, decimal

decimal.getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG    = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG    = 'No Unique Parallel Component Found'
    NO_UNIQUE__ORTHOGONAL_COMPONENT_MSG = 'No Unique Orthogonal Component Found'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG  = 'Only Defined in Two or Three Dimensions'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple([decimal.Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __getitem__(self, i):
        return self.coordinates[i]

    def __iter__(self):
        return self.coordinates.__iter__()

# LINEAR ALGEBRA METHODS
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
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return decimal.Decimal(math.sqrt(sum(coordinates_squared)))

    # Normalize a vector to find its unit vector which represents the direction.
    # u = (1/mag(v))*v
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(decimal.Decimal('1.0')/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

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

            #Capture within range of dot product to be within 1 & -1
            u1u2dot = replace_if_within_tolerance(u1.dot(u2),1)
            u1u2dot = replace_if_within_tolerance(u1.dot(u2),-1)
            angle_in_radians = math.acos(u1u2dot)

            if in_degrees:
                return math.degrees(angle_in_radians)
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
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
                self.angle_with(v) == math.pi )

    def is_zero(self, tolerance = 1e-10):
        # returns true if magnitude is less than tolerance
        return self.magnitude() < tolerance

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                                -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                  raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / decimal.Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()

# PROJECTION METHODS
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE__ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e    
    
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


# HELPER FUNCTIONS
def replace_if_within_tolerance(val, compared_against, tolerance = 1e-10):
    if abs(val - compared_against) < tolerance: return compared_against
    else: return val

