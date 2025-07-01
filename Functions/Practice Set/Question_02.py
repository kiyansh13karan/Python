# Write a python program using function to convert Celsius to Fahrenheit.


def celsius_to_fahrenheit(celsius) :
    return (celsius * 9/5) + 32

# Example usage:
c = float(input("Enter temperature in Celsius : "))
f = celsius_to_fahrenheit(c)
print(f"{c}°C is equal to {f}°F")