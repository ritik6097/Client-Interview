#Code which Explain about the method overriding
class Animal:
    def myfunc(self):
        print("Animal walk");
class Dog(Animal):
    def myfunc(self):
        print("Dog Wlk");
class Cat(Animal):
    def myfunc(self):
        print("cat walk");
obj1=Animal();
obj2=Dog();
obj3=Cat();
print(obj1.myfunc());
print(obj2.myfunc());
print(obj3.myfunc());

#Write a code where multi inheritence is explained
class Animal:
    def __init__(self,name):
        self.name=name;
    def eat(self):
        print(f"{self.name} is eating");
class Flyable:
    def fly(self):
        print("bird is flying");
class Bird(Animal,Flyable):
    def __init__(self,name):
        Animal.__init__(self,name);
        Flyable.__init__(self);
    def myfunc(self):
        print("Birds chirps");
obj=Bird("Parrot");
print(obj.eat());
print(obj.fly());
print(obj.myfunc());

#Write a code example where instance and class methods are defined in python:
class Ritik:
    height=80;  #class variable
    def __init__(self,salary):
        self.salary=salary; #instance variable
    def instance_method(self):
        print(f"salary of ritik is:- {self.salary}");
    def class_method():
        print("Class method is working as expected");
obj=Ritik(58000);
print(obj.instance_method());
print(Ritik.class_method());

#Example of __str__:-
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __str__(self):
        return f"Name:{self.name} and Age:{self.age}";
p1=Person("Seena",26);
print(p1.__str__());

#Example that Encapsulation in Python:-
class Car:
    def __init__(self,maker,model,year):
        self.__maker=maker;
        self.__model=model;
        self.__year=year;
    def get_maker(self):
        return self.__maker;
    def get_model(self):
        return self.__model;
    def get_year(self):
        return self.__year;
    def set_maker(self,maker):
        self.__maker=maker;
    def set_model(self,model):
        self.__model=model;
    def set_year(self,year):
        self.__year=year;
car=Car("Toyato","V5",1994);
car.get_maker();
car.get_model();
car.get_year();
car.set_maker("maruti");
car.set_model("V8");
car.set_year(1997);
print(car.get_model());

    