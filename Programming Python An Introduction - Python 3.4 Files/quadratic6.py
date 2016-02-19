# quadratic6.py

import math

def main():
    print('This program finds the real solutions to a quadratic\n')

    try:
        a, b, c = eval(input('Please enter the coefficents (a, b, c): '))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        if root1 == root2:
            print('The quadratic has a double root at:', root1)
        else:
            print('The roots are:', root1, root2)
    except ValueError as exc0bj:
            if str(exc0bj) == 'math domain error':
                print('No real Roots.')
            else:
                print("You didn't give me the right number of coefficents")
    except NameError:
            print("\nYou didn't enter three numbers")
    except TypeError:
            print("\nYour inputs were not all numbers")
    except SyntaxError:
            print("\nYour input was not in the correct form.  Missing comma?")
    except:
            print("\nSomething went wrong")

if __name__ == '__main__':
    main()
    
