# This program calculates the volume and surface of a shphere, given it's radius.

import math

def main():

    print("This program will calculate the Volume and Surface Area of a sphere.")
    R = eval(input("Input the radius of the sphere: "))

    V = (4/3) * math.pi * (R**3)
    A = 4 * math.pi * (R**2)

    print ("The Volume is", round(V,3) ,"cubic units.")
    print ("The Surface Area is", round(A,3),"square units.")

main()

