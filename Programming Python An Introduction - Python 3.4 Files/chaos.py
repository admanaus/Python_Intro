#  File: chaos.py
#  A simple program demonstrating caotic behavior.

def main():
    print("This program illistrates a chaotic function")
    x1 = eval(input("Enter a number between 0 and 1: "))
    x2 = eval(input("Enter another number between 0 and 1: "))
    y = eval(input("Enter the number of iterations: "))
    print ("   First Value: ",x1,"   Second Value: ",x2)
    print ("================================")

    for i in range(y):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print ("      ",round(x1,6),"        ",round(x2,6))

main()
