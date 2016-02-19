# This program will calculate the cost per square inch of pizza, based on diameter.

import math

def main():
    print("This program will calculate the cost per square inch of pizza.")
    Number = eval(input("Enter the number of pizzas you would like to compare: "))
    C = 1

    for i in range (Number):    
        print("Enter the price of Pizza", C ,": $")
        Price = eval(input())
        print("Enter to diameter of Pizza", C ,"in inches:")
        Diam = eval(input())
        x = Price / (math.pi * ((Diam/2)**2))
        print ("The cost per square inch of pizza",C,"is: $", round(x,3))
        C = C + 1

main()
