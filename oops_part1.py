#Vehicle class without any variable and method
class Vehicle:
    pass;


#Creating a class Person and it's object:-
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
p1=Person("RITIK",23);
print(p1.name);
print(p1.age);

#Create and call method of class in Python
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def myfunc(self):
        print("MY NAME IS:-"+self.name);
p1=Person("RITIK",23);
print(p1.name);
print(p1.age);
print(p1.myfunc());

#update object properties in Python

class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def myfunc(self):
        print("MY NAME IS:-"+self.name);
p1=Person("RITIK",23);
p1.name="RITIKA";
print(p1.name);
print(p1.age);
print(p1.myfunc());

#delete object properties and object in Python:-
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def myfunc(self):
        print("MY NAME IS:-"+self.name);
p1=Person("RITIK",23);
p1.name="RITIKA";
del p1.age;
print(p1.name);
print(p1.age);
print(p1.myfunc());

