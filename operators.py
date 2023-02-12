# We use operators to manipulate the value of operands (Values/Variables)
# Types of operators
# 1. Arithmetic operators (+,-,/,*,%,**,//)
# 2. Comparison operators (>,<,<=,>=,!=,==)
# 3. Assignment Operators (=,+=,-=,*=,%=,**=,//=)
# 4. Logical Operators (and,or,not)


# COMPARISON OPERATORS
# == equal to sign
# != not equals to sign
# < less than sign
# > greater than

a = 4
b = 5

# equal
print('a == b :', a == b)

# not equal
print('a !=b :', a == b)

# greater than
print('a > b :', a > b)

#  less than
print('a < b :', a < b)

# greater than equals to
print('a.=.b :', a >= b)

# less than or equal to
print('a<=b :', a <= b)

# assignment operators
# = assignment operator
# -= subtraction
# += addition
# /= division
# *= multiplication
# %= remainder
# //= floor division
# **= exponent

c = 6
c += 5
c -= 4
c = c + 5
# assignment operators
a = 10
# addition
a += 5
print('a += 5, ', a)
# subtraction
a -= 5
print('a -=5 ', a)
# multiplication
a *= 5
print('a *= 5', a)
# division
a /= 5
print('a /= 5', a)
# remainder
a %= 3
print('a %= 3', a)
# exponent
a **= 2
print('a **= 2', a)
# floor division
a //= 3
print('a //= 3', a)

# logical operator
# and logical and if both statements are true
# or logical or if both statements are non zero

# decision-making process
# in decision-making process in python if and else statement

variablecompare = 10
secondvariable = 5

if variablecompare == 7:
    print('condition met')
else:
    print('condition not met')

    # multi conditional
    if variablecompare == 10:
        print('multi condition met')
    elif variablecompare == 7:
        print('multi condition not met')
    elif variablecompare == 6:
        print('from multi conditional')
    else:
        print('none meets condition')

        #
    if variablecompare == 6 or secondvariable == 5:
        print('from or')




































