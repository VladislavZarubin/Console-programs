# function declaration
def is_correct_bracket(text):
    ''''This function checks the number of open 
    and closed brackets in typed expression an expression'''
    flag = True
    counter = 0
    for c in text:
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
            if counter < 0:
                break
    if counter != 0:
        flag = False
    return flag

# input data
txt = input("- - - Enter your expression: - - -\n")

# call function
if is_correct_bracket(txt) is True:
    print("- - - Correct number of brackets! - - -")
else:
    print("- - - Wrong number of brackets! - - -")
