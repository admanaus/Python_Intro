# This program uses a loop to find the factorial of a number.

def main():

    print("This program will find the factorial of a number.")
    print()
    n = eval(input("Enter a number: "))
    fact = 1
    
    for factor in range (2,n+1):
        fact = fact * factor
    
    print("The factorial of",n,"is", fact)

main()
