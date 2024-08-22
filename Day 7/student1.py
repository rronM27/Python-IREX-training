class Student:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    #we deal with age here

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age


student1 = Student('Alma', 18)
student2 = Student('Agon', 20)
print(student1.age)
print(student2.age)