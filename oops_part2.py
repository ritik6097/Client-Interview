#Copy all proprties from an object to another object:
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
P1=Person("RITIK",23);
P2=Person(" ",0);
P2.__dict__.update(P1.__dict__);
print(P2.name);
print(P2.age);

#print all properties of an object in PYTHON:-

class Project:
    def __init__(self,domain,yoe,name):
        self.domain=domain;
        self.yoe=yoe;
        self.name=name;
def print_properties(obj):
    dict=vars(obj);
    for k,v in dict.items():
        print(k,':',v);
obj=Project("PYTHON",2,"RITIK");
print(print_properties(obj));

#Creating data attributes of a class in run time

class Employee:
    pass;
e1=Employee();
setattr(e1,'age',25);
setattr(e1,'name',"RITIK");
print(e1.age);
print(e1.name);

#create and use custom self parameter in Python
class Employee:
    def __init__(self,name,salary):
        self.name=name;
        self.salary=salary;
    def myfunc(self,custom_param):
        print(f"{custom_param} + {self.salary}");
custom_param="Employee Salary is:-";
obj=Employee("RITIK",58000);
obj.myfunc(custom_param);

#Create and use static class variable in Python:-
class Demo:
    mypointer=0;
    def __init__(self):
        Demo.mypointer=Demo.mypointer+1;
    def get_pointer(self):
        return Demo.mypointer;
obj1=Demo();
obj2=Demo();
obj3=Demo();
print(obj1.get_pointer());
print(obj2.get_pointer());
print(obj3.get_pointer());

