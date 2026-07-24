is_authenticated = True
is_admin = True

if is_authenticated:
    print('You are logged In.')
    
    if is_admin:
        print("You can access dashboard.")
    else:
        print("You are not authorized.")    
else:
    print('You are not logged In.')    