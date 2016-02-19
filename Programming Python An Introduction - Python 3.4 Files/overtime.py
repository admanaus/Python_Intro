# overtime.py
#   This program claculates a weekly paycheck based on time worked

def main():
    try:
        print("This program wil calculate a weekly paycheck, and account for overtime.\n")
        wage = eval(input("Input the hourly wage:"))
        hours = eval(input("Input the hours worked this week:"))
        overtime = hours - 40
    
        if hours > 40:
            pay = (overtime * wage * 1.5) + (40 * wage)
            print("$", round(pay, 2), "is due.")
            print(round(overtime,2), "hours of overtime were worked.")
            print("$", pay - (40 * wage), "was paid in overtime.")
        else:
            pay = hours * wage
            print("$", round(pay, 2), "is due.")
            
    except:
       print("Something went wrong, please try again")
        
if __name__ == "__main__":
    main()
