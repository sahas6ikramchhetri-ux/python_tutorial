# for loop with range(start,stop)
for num in range(1,11):
    print(num)


# for loop with range(start,stop,step)
for num in range(1,11,2):
    print(num)    


# for loop with string
username = "suresh"    

for txt in username:
    print(txt)

# for loop with list
hobbies = ["coding","treking","football"]    

for hobbie in hobbies:
    print(hobbie)
else:
    # optional (execute after loop is finished)
    print("End of list.")    


# example: check is number is +ve, -ve or zero in list    
numbers = [10,-20,30,0,-11]

for num in numbers:
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero.")        


for num in numbers:
    if num == 0:
        print(f"{num} is invalid.")
    elif num % 2 == 0:
        print(f"{num} is even number.") 
    else:
        print(f"{num} is odd number.")               
        

# for loop with break
for num in range(1,6):
    if num == 3:
        break
    print(num)        


# for loop with continue
for num in range(1,6):
    if num == 3:
        continue
    print(num)            