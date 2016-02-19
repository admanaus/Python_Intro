# month.py

#   A program to print the abbriviation of a month, given a number

def main():
    # months is used as a look up table
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'

    for i in range(12):
        n = eval(input('Enter a month number (1-12): '))

        # compiute starting position of month in n months
        pos = (n-1) * 3

        # grab the appropriate slice from the month string
        monthAbbrev = months[pos:pos+3]

        # print the result
        print ('The month abbriviation is:', monthAbbrev + '.')

main()
    
    
