## review
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

    def print(self):
        print("this is a animal")

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a attribute named name
        self.name = name
    
    def print(self):
        print("This is a dog")
    
## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a attribute named name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a attribute named name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## employee has-a attribute named salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person('Mary')

## from mary the pet attribute is-a satan?
mary.pet = satan

## frank is-a employee, his salary is 120000
frank = Employee("Frank", 120000)

## from frank the pet attribute is-a rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


test = Animal()
test.print()
# Animal.print()
dg = Dog('asd')
dg.print()
print(dg.name)