class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"My name is {self.name}, i am {self.age} years old, and my gender is {self.gender}")

person1=Person('Entrix Makambi',23,'Male')

person1.introduce()