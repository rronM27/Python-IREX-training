class klasa:
    def gjuhaprogramimit(self):
        pass

class Student(klasa):
    def __init__(self, name,gjuhaprogramuese):
        self.name = name
        self.gjuhaprogramuese = gjuhaprogramuese

    def gjuhaprogramimit(self,):
        return self.gjuhaprogramuese

class Teacher(klasa):
    def __init__(self, name,gjuhaprogramuese, level):
        self.name = name
        self.gjuhaprogramuese = gjuhaprogramuese
        self.level = level

    def gjuhaprogramimit(self,):
        return self.gjuhaprogramuese
    def level(self):
        return self.level

alma=Teacher('alma',5,"adv")
Olta=Student('olta',8)
