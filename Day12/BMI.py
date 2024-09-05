from abc import ABC, abstractmethod
import streamlit as st

class Person(ABC):
    """
    Abstract base class representing a person.
    """

    def __init__(self, name, age, weight, height):
        """
        Initializes a new instance of the Person class.
        """
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        """
        Gets the weight of the person.

        Returns:
            float: The weight of the person.
        """
        return self._weight

    @weight.setter
    def weight(self, value):
        """
        Sets the weight of the person.

        Raises:
            ValueError: If the weight is negative.
        """
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        """
        Gets the height of the person.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the person.

        Raises:
            ValueError: If the height is negative.
        """
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        """
        Calculates the BMI of the person.
        """
        pass

    @abstractmethod
    def get_bmi_category(self):
        """
        Gets the BMI category of the person.
        """
        pass

    def print_info(self):
        """
        Prints the information of the person, including BMI and category.
        """
        print(f"{self.name}, Age: {self.age}, Weight: {self.weight} kg, Height: {self.height} m, "
              f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")


class Adult(Person):
    """
    Subclass representing an adult person.
    """

    def calculate_bmi(self):
        """
        Calculates the BMI of the adult using the formula weight/(height^2).
        """
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        """
        Gets the BMI category of the adult.
        """
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    """
    Subclass representing a child person.
    """

    def calculate_bmi(self):
        """
        Calculates the BMI of the child using the formula weight/(height**2)*1.3
        """
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        """
        Gets the BMI category of the child.
        """
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"


class BMIApp:
    """
    Class representing the BMI application.
    """

    def __init__(self):
        """
        Initializes a new instance of the BMIApp class.
        Creates an empty list to store Person objects.
        """
        self.people = []

    def add_person(self, person):
        """
        Adds a person to the list of people.
        """
        self.people.append(person)

    def collect_user_data(self):
        """
        Collects user data from the console and creates a Person object.
        """
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        self.add_person(person)

    def print_results(self):
        """
        Prints the results for all collected people.
        """
        for person in self.people:
            person.print_info()

    def run(self):
        """
        Runs the BMI application, collecting user data and printing results.
        """
        while True:
            self.collect_user_data()
            cont = input("Do you want to add another person? (yes/no): ").strip().lower()
            if cont != 'yes':
                break
        self.print_results()


# Create an instance of BMIApp and run the application
app = BMIApp()
app.run()
