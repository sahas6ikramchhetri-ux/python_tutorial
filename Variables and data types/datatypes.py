# string data types -> use for text
message = "This is my message."
print(type(message))

# int data type -> use for integer
age = 24
print(type(age))

# float data type -> use for decimal number
price = 99.99
print(type(price))

# boolean data type -> only have two value (True or False)
is_admin = True 
is_verified = False
print(type(is_admin))

# list -> used to store multiple data
# ordered, mutable and allow duplicate
hobbies = ["coding","treking","football"]
print(type(hobbies))

# tuple -> used to store multiple data
# ordered, unmutable and allow duplicate
numbers = (10,30,23,34,55)
print(type(numbers))

# set -> used to store multiple data
# unordered, mutable and donot allow duplicate
numbers = {10,30,23,34,55}
print(type(numbers))

# dictionary -> collection of key-value pairs
# ordered, mutable and donot allow duplicate
student = {
    "id": 101,
    "full_name": "Suresh Thapa",
    "is_verified": True,
    "subjects": ["math","science","english"],
    "address": {
        "country": "Nepal",
        "street": "Kathmandu",
        "zipcode": 44600
    }
}
print(type(student))

# None data type -> represent no value or null value
user = None
print(type(user))

# complex data type
num = 3 + 4j
print(type(num))