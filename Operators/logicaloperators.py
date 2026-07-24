is_logged_in = True
is_verified = True
is_admin = False

# 1. and operator -> return True if all condition is True else return False 
print(f"And 1: {is_logged_in and is_verified}")
print(f"And 2: {is_logged_in and is_verified and is_admin}")

# example
age = 19
has_nid = True

eligible = age >= 18 and has_nid
print(f"Is eligible: {eligible}")

# 2. or operator -> return True if atleast one condition is True else return false

print(f"Or 1: {is_logged_in or is_verified}")
print(f"Or 2: {is_logged_in or is_verified or is_admin}")

# example 
has_citizenship = False
has_nid = False

can_withdraw = has_citizenship or has_nid
print(f"Can withdraw: {can_withdraw}")

# example -> with both 'and' and 'or' operator
# user must be 18 or above and must have nid or citizenship
age = 18
has_citizenship = True
has_nid = True

can_vote = age >= 18 and (has_citizenship or has_nid)
print(f"Can vote: {can_vote}")

# 3. not operator -> convert True to False and vice-versa
print(f"Not 1: {not is_logged_in}")
print(f"Not 2: {not is_admin}")