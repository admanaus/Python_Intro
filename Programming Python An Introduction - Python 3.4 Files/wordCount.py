# wordCount.py
#   This program counts the words in a file.

def main():

    inFileName = input('What file would you like to count the words in? ')

    inFile = open(inFileName, 'r') # open the file

    count = 0
    
    for word in inFile.read().split():    
        count = count + 1
        
            
    print('The file contains', count, 'words.')

main()
    
