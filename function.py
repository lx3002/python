#
#
#
#
#
#
# should be used by def
#  to call function we use name of the function followe by set of brackets


def greeting():
    # write the logic /block of the code function
    print('hello from checkout')
    return


greeting()
message = 'hello from user'


def greetings_from_user(greet):
    print(greet)
    return


greetings_from_user(message)


def simple_add(num1, num2):
    print(int(num1) + int(num2))
    return


simple_add(8, 8)

result = 0
# ANNONYMUS FUNCTIONS ARE NOT DEFINED BY DEF KEYWORD BY LAMDA
# CAN ONLY RETURN ONLY ONE VALUE IN FORM OF EXPRESSION
# CAN ONLY ACCESS GLOBAL VARIABLES AND LISTED PARAMETERS
# TO WORK THEM WELL  STORE THE LAMDAS FUNCTION INSIDE A VARIABLE
sum = lambda num1, num2: num1 + num2
print('value of', sum(10, 10))








