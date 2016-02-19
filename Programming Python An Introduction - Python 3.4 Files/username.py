# username.py

#   Simple string processing prgram to generate usernames

def main():
    print('This program generateds user names. \n')

    # get users first and last names
    first = input('Please enter your first name (all lowercase): ')
    last = input('Please enter your last name (all lowercase): ')

    # concatenate first initial with 7 chars of last name
    uname = first[0] + last[:7]

    # output the username
    print ('Your username is:', uname)

main()
