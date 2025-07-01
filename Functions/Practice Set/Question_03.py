# Write a program which converts inches to cms.


def inches_to_cms(inches) :
    return inches * 2.54

inches = float(input("Enter length in inches : "))
cms = inches_to_cms(inches)
print(f"{inches} inches is equal to {cms} centimeters.")