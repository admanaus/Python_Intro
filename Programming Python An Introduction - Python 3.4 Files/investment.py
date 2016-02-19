# Determins the future value of an account.

def main():
    print("This program will determint the future value of an account.")

    principal = eval(input("What is the initial value of the account? "))
    apr = eval(input("What is the annual percentage rate as a decimal? i.e.(0.03) "))
    time = eval(input("How many years will the account be active? "))

    for i in range(time):
        principal = principal * (1 + apr)

    print("The final value of the account will be $",principal)

main()
