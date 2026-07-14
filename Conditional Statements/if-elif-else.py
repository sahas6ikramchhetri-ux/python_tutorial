grade = 65

if grade > 90:
    print('A+')
elif grade > 80:
    print('A')
elif grade > 70:
    print('B')
elif grade > 60:
    print('C')
else:
    print('F')                


# example -> check if number is +ve, -ve or zero
num = int(input("Enter a number: "))

if num > 0:
    print('Positive')
elif num < 0:
    print("Negative")
else:
    print('Zero')            