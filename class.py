class Human:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
    
    def do_work(self):
        if self.occupation == "doctor":
            print(self.name," is a doctor")
        else:
            print(self.name," is not a doctor")

tom = Human("Tom cruise","actor")
tom.do_work()

class Doctor(Human): # in case of multiple inheritence just add  more classes here
    def __init__(self,name):
        super().__init__(name,"doctor")

john = Doctor("John Mathew")
john.do_work()
# special functions
# check object
print(isinstance(john,Doctor)) # True
issubclass(Doctor,Human) # True