# dateConvert2.py

#   Converts a numeric date (12/7/2010) into a text date (December 12, 2010)

def main():
    print('This program will convert a nemeric date into a text date.')
    dateStr = input('Enter a date (mm/dd/yyyy): ')
    monthStr, dayStr, yearStr = dateStr.split('/')

    # find the month
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October',
              'November', 'December']
    monthStr = months[int(monthStr)-1]
    
    # display converted date
    print(monthStr,dayStr+',',yearStr)

main()
