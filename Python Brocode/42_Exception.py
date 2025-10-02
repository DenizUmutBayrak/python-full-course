#exception = An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)ü
#            1.try, 2.except, 3.finally

#1/0 ZeroDivisionError
# 1 + "1"  TypeError
#int("pizza") Value Error

try:
    number = int(input("Enter a number "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You have divide by number")
except Exception:
    print("Something went wrong")
finally:
    print("Do some clean up here")


"""
try:
    #Try some code
except Exception:
    #Handle an Exception
finally:
    #Do some clean up
"""