# function declaration
def is_password_good(password):
    flag = True
    for char in '1234567890':
        if char in password:
            flag = True
            break
        else:
            flag = False
    if len(password) < 8:
        flag = False
    if password == password.lower():
        flag = False
    if password == password.upper():
        flag = False  
    return flag

# data input
txt = input()

# call function
print(is_password_good(txt))