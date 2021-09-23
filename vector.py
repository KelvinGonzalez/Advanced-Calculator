from math import sqrt, cos, acos, degrees, radians


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        # Calculate the length of the vector
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self):
        # Return only the direction of the vector
        return self / self.magnitude()

    def __add__(self, other):
        # Add 2 vectors
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # Subtract 2 vectors
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        # Multiply a vector and a scalar
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        # Divide a vector and a scalar
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        # Calculate the dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle(self, other):
        # Calculate the angle between 2 vectors
        return degrees(acos(self.dot(other) / (self.magnitude() * other.magnitude())))

    def projection(self, other):
        # Calculate the projection
        return other * (self.dot(other) / pow(other.magnitude(), 2))

    def cross(self, other):
        # Calculate the cross product
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def scalarTripleProduct(self, v2, v3):
        # Calculate the scalar triple product
        return self.dot(v2.crossProduct(v3))

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    @staticmethod
    def API():
        return "Vector API:\nVector.x\nVector.y\nVector.z\nVector + Vector\nVector - Vector\nVector * Scalar\nVector / Scalar\nstr(Vector)\nVector.magnitude()\nVector.normalized()\nVector.dot(Vector)\nstaticDot(Magnitude, Magnitude, Angle)\nVector.angle(Vector)\nVector.projection(Vector)\nVector.cross(Vector)\nVector.tripleScalarProduct(Vector, Vector)\nVector2(x, y)"

    @staticmethod
    def Vector2(x, y):
        # Create a 2D vector
        return Vector(x, y, 0)

    @staticmethod
    def staticDot(magnitudeA, magnitudeB, angle):
        # Calculate the dot product with the given parameters
        return magnitudeA * magnitudeB * cos(radians(angle))
