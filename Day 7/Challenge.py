#define a base class name digital school with the following
class DigitalSchool:

#private attributes: name,city,state,course
#constructor __name - this is private name - this is not
    def __init__(self, name, city, state, courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

# getter and setter for all attributes with the @property method
    @property
    def name(self):
          return self.__name
    @name.setter
    def name(self, name):
         self.__name = name
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        self.__city = city
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
    @property
    def courses(self):
        return self.__courses

# methords: show_school_info returns a dictionary with school info and
    def show_school_info(self):
        return{
            'name':self.__name,
            'city':self.__city,
            'state':self.__state,
            'courses':self.__courses,
        }

#method2 : organize_hackthone(): define a placeholder method to overridden by subclasses
    def organize_hackthone(self):
        print("Organize a generic hackthone")






# define DS_Prishtina inheritance from Digital School as a superclass:
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses,student_number):
        super().__init__(name,city,state,courses)
        self.__student_number = student_number

# constructor where we add a new private atribute student_number
    @property
    def student_number(self):
        return self.__student_number
    @student_number.setter
    def student_number(self, student_number):
        self.__student_number = student_number



# add two methods SCF() -> print out a specific message as Welcome to SCF and define organize_hackathone again
    def SCF(self):
        print("first edition")

    def organize_hackthone(self):
        print("Organize a super hackthone")



prishtina_obj=DS_Prishtina("Digital School Prishtina Pejton","Prishtina",
                           "Kosova",["Python","CSS","JS"],100)
prishtina_obj.SCF()
print(prishtina_obj.student_number)