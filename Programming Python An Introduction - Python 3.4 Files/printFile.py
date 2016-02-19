# printFile.py

#   This simple program prints a text file to the screen

def main():
    fname = input('Enter a file name: ')
    infile = open(fname,'r')
    data = infile.read()
    print(data)

main()
