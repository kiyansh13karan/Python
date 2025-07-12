'''
Write __str__() method to print the vector as follows: 
    7i + 8j +10k  
Assume vector of dimension 3 for this problem.
'''



class Vector:
    def set_values(self, values):
        if len(values) != 3:
            raise ValueError("This vector class only supports 3 dimensions.")
        self.values = values

    def __str__(self):
        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"


v = Vector()
v.set_values([7, 8, 10])
print(v)  # This will call __str__()
