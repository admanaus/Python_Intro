# numbers2text.py

#   A program to convert a sequence of Unicode numbers into text

def main():
    print('This program converts a sequence of Unicode numbers into')
    print('the string of text it represents./n')

    # Get the message to encode
    inString = input('Please enter the Unicode-encoded message: ')

    # Loop through each substring and build Unicode message
    message = ''
    for numString in inString.split():
        codeNum = eval(numString)   # Converts digits into a number(string to intiger)
        message = message + chr(codeNum) # concates character to message
        print(message)
    print('\nThe decoded message is: ', message)

main()
