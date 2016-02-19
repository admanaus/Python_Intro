##A simple program to find an average

def main():
    print("This program will average calculate the of test scores.")
    x = eval(input("How many scores would you like to average? "))
    z = 0
    
    for i in range(x):
        y = eval(input("Enter each score:"))
        z = y + z

    print("The average is: ",(z/x))

main()





