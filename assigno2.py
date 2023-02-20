class Person:
    def info_self(self):
        print('my name is' + self.name)

 age = 18
try:
    print(age)
except:
    print("An error occured , check if email is defined")
else:
    print(str(age) + " from else") # try not to do the same thing as in try
finally:
    print("Finally block")  # try not to do the same thing as in try

# raise keyword : works with a condition if condition is met , raise an error message/exception/typeerror
if age < 18:
  raise Exception("sorry x shouldn't be less than zero")

voter = Person()
voter.name = 'tom'
voter.age = 30
voter.gender = 'male'


# print("voter.name: {}\nvoter.age: {}\nvoter.gender: {} ".format(voter.name, voter.age, voter.gender, ))
def details(voter):
    print("My name is {}".format(voter.name))
    print("My gender is {}".format(voter.gender))
    print("My age is {}".format(voter.age))

a = Person('name','age','gender')
a.details()





















