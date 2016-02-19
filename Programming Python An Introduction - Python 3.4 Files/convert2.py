# convert2.py
#   A program to convert Celsius temps into Farenheit.
#   This version issues heat and cols warnings

def main():
    celsius = eval(input('What is the Celesius tempeture? '))
    farenheit = 9/5 * celsius + 32
    print('The tempeture is:', farenheit, 'degrees Farenheight today.')

    # Print a warning for extreme temps
    if farenheit > 90:
        print("It's really hot out there.  Be careful.")

    if farenheit < 30:
        print("Brrrr.  Be sure to dress warmly")

main()
