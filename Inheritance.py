class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def ShowName(self):
        print(self.fname, self.lname)
p1 = Person("Eugene","Asare")

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def Welcome(self):
        print(f"Welcome Master", self.fname , self.lname , "to the class of" , self.graduationyear ,"graduation party!")


s1 = Student("Kofi","Asare",2022)
s1.Welcome()