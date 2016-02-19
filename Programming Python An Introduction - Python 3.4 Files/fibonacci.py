# fibonacci.py
#   This program will display the Fibbinacci sequence to the Nth degree.

def main():
    print("This program will display the Fibbinacci sequence to the Nth value\n")
    number = eval(input("Enter the number of values you would like to see:"))
    first = 1
    second = 1
    print(first, "", end = "")
    print(second, "", end = "")

    while True:
        third = first + second
        print(third, "", end = "")
        first = second
        second = third
        number = number - 1
        if number <= 0:
            break
    print("\nThe last number in the sequence was:", third)

if __name__ == "__main__":
    main()
    
    
