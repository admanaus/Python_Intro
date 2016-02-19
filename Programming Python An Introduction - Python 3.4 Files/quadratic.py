# quadratic.py
# A program that computes the real roots of a quadratic formula.
# Illistrates use of the math library

# Note: This program crashes if the equation has no real roots.

import math  # Makes the math library avalible

def main():
    print("This program finds the real solutions to a quadratic.")
    print()

    a, b, c = eval(input("Please enter the coefficents (a, b, c): "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1,"and ", root2)

main()
          
                   
