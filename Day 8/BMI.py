from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name,age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height
    @property
    def weight(self):
        return self.weight
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if height<0:
            raise ValueError('Height is negative')
        self._height = height

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height},"
              f" BMI: {self.calculate_bmi()}, Category: {self.get_bmi_category()}")

    class Adult(Person):
        def calculate_bmi(self):
            return self.weight / self.height /**2

        def get_bmi_category(self):
            ibm=self.get_bmi_category()
            if ibm < 18.5: return "Underweight"
            elif 18.5 <= ibm < 25: return "Normal"
            elif 25 <= ibm < 30: return "Overweight"
            elif ibm >= 30: return "Obesity"



class Child(Person):
    def calculate_bmi(self):
        return (self.weight / self.height**2)*1.3
    def get_bmi_category(self):
        bmi=self.get_bmi_category()
        if bmi < 14: return "Underweight"
        elif  14 <= bmi < 17: return "Normal"
        elif 17 <= bmi < 25: return "Overweight"
        elif bmi >= 25: return "Obesity"


class BMIApp:
    def __init__(self):
        self.people=[]
    def add_person(self, person):
        self.people.append(person)
    def collect_user_data(self):
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        weight=float(input("Enter your weight: "))
        height=float(input("Enter your height: "))
        if age>=18:
            person=Adult(name,age,weight,height)
        else:
            person=Child(name,age,weight,height)
            self.people.append(person)

    def print_results(self):
        for person in self.people:
            person.print_info()
    def run(self):
        while True:
            self.collect_user_data()
            cont=input("Do you want to add another person(y/n)? ")
            if cont!='y':
                break
            self.print_results()
app=BMIApp()
app.run()



