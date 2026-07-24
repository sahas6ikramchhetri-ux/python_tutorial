# print from 1 to 10 using while loop
num = 1

while num <= 10:
    print(num)
    num += 1


# example: username and password with 3 attempts    
correct_username = "admin"   
correct_password  = "12345"

attempts = 3

while attempts > 0:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print('Login Successful!')
        break   # break out of loop
    else:
        attempts -= 1  # decrement attempts by 1
        print("Invlaid username or password!")
        print(f"Attempts left: {attempts}")
    

if attempts == 0:
    print("Account locked! Too many failed attempts!")    
    
    