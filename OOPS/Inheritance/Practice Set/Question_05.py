'''
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them.
'''



class Vector:
    def set_values(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same dimension for addition.")
        result = Vector()
        result.set_values([a + b for a, b in zip(self.values, other.values)])
        return result

    def __mul__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.values, other.values))

    def display(self):
        print("Vector:", self.values)



v1 = Vector()
v1.set_values([1, 2, 3])

v2 = Vector()
v2.set_values([4, 5, 6])

# Vector Addition
v_sum = v1 + v2
print("Sum of Vectors:")
v_sum.display()

# Dot Product
dot_product = v1 * v2
print("Dot Product:", dot_product)
