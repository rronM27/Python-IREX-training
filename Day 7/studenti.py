class Student:
    def __init__(self, name, age,):
        #initialize private attributes
        self.__name = name
        self.__age = age
    #this is a getter method for attribute name
    def get_name(self):
        return self.__name

    #this is a setter
    def set_name(self, name):
        self.__name = name


    #this is a getter method for attribute age
    def get_age(self):
        return self.__age

    #this is a setter
    def set_age(self, age):
        self.__age = age


student1 = Student('John', 18)
print(student1.get_name())
print(student1.get_age())
