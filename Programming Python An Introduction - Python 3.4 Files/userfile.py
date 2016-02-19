# userfile.py
#   Program to create a file of usernames in batch mode.

def main():
    print('This program creates a file of usernames from')
    print('a file of names')

    # get the file names
    inFileName = input('What file are the names in? ')
    outFileName = input('What file should the usernames go in?')

    # opent the file
    inFile = open(inFileName, 'r')
    outFile = open(outFileName, 'w')

    # process each line of the input file
    for line in inFile:
        first, last = line.split() # get the first and last name from a line
        uname = (first[0]+last[:7]).lower() # create user name
        print(uname, file = outFile) # write username to output file

    # close both files
    inFile.close()
    outFile.close()

main()

    
