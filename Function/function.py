# 1. basic function
def display_message():
    print("This is my message.")

# calling function
display_message()
display_message()      

# 2. function with parameters
def display_info(full_name,age):
    print(f"Full Name: {full_name} and Age: {age}")

display_info("Suresh Thapa",25)
display_info("John Doe",24)

# 3. function with return type   
def calculate_sum(num1,num2):
    return num1 + num2

res = calculate_sum(10,20)
print(f"Result: {res}")

res1 = calculate_sum(20,20)
print(f"Result: {res1}")


# 4. function with default argument
def calculate_discount(price,discount = 0.1):
    return price - (price * discount)

print(f"After discount: {calculate_discount(100)}")
print(f"After discount2: {calculate_discount(200)}")
print(f"After discount3: {calculate_discount(200,0.2)}")

# 5. function with keyword argument
def student_info(id,name,age):
    print(f"Id: {id} and Name: {name} and Age: {age}")

student_info(age=24,name="Suresh Thapa",id=101)    

# 6. *args -> allows you to recieve zero or more positional agrument
def add(*args):
    sum = 0
    for num in args:
        sum += num # sum = sum + num
    print(f"Reult: {sum}")    
        

add(10,20,30)
add(10,20,50,60,70)
add(50,77,11)    


# **kwargs -> allow function to zero or more receive keyword argument
def stud_info(**kwargs):
    print(kwargs)

stud_info(name="Suresh Thapa",age=24,is_verified=False)
stud_info(name="John Thapa",age=25)      


# Example with normal, *args and **kwargs parameters

def pizza_order(size,crust,*toppings,**customer_details):
    print(f"Size: {size}")
    print(f"Crust: {crust}")
    print(f"Toppings: {toppings}")
    print(f"Customer Details: {customer_details}")


pizza_order('Large','Thin','Cheese',"mushroom",'Olives',name="Suresh",phone="98000000")    

pizza_order('Large','Thin','Cheese',"mushroom",name="Suresh",phone="98000000",email="suresh@gmail.com") 