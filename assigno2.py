class Person:
    def info_self(self):
        print('my name is' + self.name)


voter = Person()
voter.name = 'tom'
voter.age = 30
voter.gender = 'male'


# print("voter.name: {}\nvoter.age: {}\nvoter.gender: {} ".format(voter.name, voter.age, voter.gender, ))
def details(voter):
    print("My name is {}".format(voter.name))
    print("My staff number is {}".format(voter.gender))
    print("My age is {}".format(voter.age))


a = voter('alex', 'female', 34)
a.details()
