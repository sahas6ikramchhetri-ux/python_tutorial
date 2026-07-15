numbers = [10, -20, 30, 0, -11]

for num in numbers:
    if num == 0:
        print(f"{num} is invalid")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
