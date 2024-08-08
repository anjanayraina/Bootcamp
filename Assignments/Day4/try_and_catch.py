try :
    divident = int(input())
    divisor = int(input())
    result = divident/divisor
    print(result)
except ZeroDivisionError :
    print("Divison by 0")
except ValueError :
    print("Give the values in the right format")
finally :
    print("Finally block")
