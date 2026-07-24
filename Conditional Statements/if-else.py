# if statement

age = 17

if age >= 18:
    # only execute if condition is True
    print("You can vote.")


# if-else
if age >= 18:
    # only execute if condition is True
    print("You can vote.") 
else:
    # only execute if condition is False
    print("You cannot vote.")       


# ternary operator -> shorthand for if-else  
# syntax: true-statement if condition else false-statement  

print("You can vote.") if age >= 18 else print("You cannot vote.")



# example with and operator
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == 'admin' and password == '1234':
#     print("You are loggedin sucessfully.")
# else:
#     print("Invalid username or password!")    


# example with not operator    
is_authenticated = False

if not is_authenticated:
    print("You are not logged In.")