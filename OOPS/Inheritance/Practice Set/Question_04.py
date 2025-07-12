'''
Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them.
'''


class Complex:
    def set_values(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        result = Complex()
        result.set_values(self.real + other.real, self.imag + other.imag)
        return result

    def __mul__(self, other):
        result = Complex()
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        result.set_values(real_part, imag_part)
        return result

    def display(self):
        print(f"{self.real} + {self.imag}i")




c1 = Complex()
c1.set_values(3, 2)

c2 = Complex()
c2.set_values(1, 7)

# Addition
sum_result = c1 + c2
print("Sum:")
sum_result.display()

# Multiplication
product_result = c1 * c2
print("Product:")
product_result.display()
