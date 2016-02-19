# averageFromFile.py
#   This program claculates the average of numbers contained in a file

def main():
    try:
        print("This program wil calculate the average of numbers contained in a file.\n")
        fileName = input("What file are the numbers in?")
        inFile = open(fileName,'r')
        sum1 = 0.0
        count = 0
        line = inFile.readline()
        while line != "":
            # update sum and count for values in line
            for xStr in line.split(","):
                sum1 = sum1 + eval(xStr)
                count = count + 1
            line = inFile.readline()
        print("\nThe average of the numbers is", sum1 / count)
            
    except:
       print("Something went wrong, please try again")
        
if __name__ == "__main__":
    main()
