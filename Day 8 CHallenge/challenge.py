class Person:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.__weight = weight
        self.__height = height

    def name(self):
        return self.name
    def age(self):
        return self.age
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
        return self.__weight

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height
        return self.__height

    class Adult(Person):
         get_BMI= weight/height
        def __init__(self,calculate_bmi, get_bmi_category):
            self.calculate_bmi = calculate_bmi()
            self.get_bmi_category = get_bmi_category
            if BMI < 18.5
                print("Underweight")
                if 18.5 <= BMI < 24.9
                    print("Normal weight")
                    else 24.9 <= BMI < 29.9
                        print("Overweight")
                        elif BMI >= 29.9
                    print("Obese")
    weight=70
    height=1.70

    class Child(Person):


