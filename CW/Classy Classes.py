class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f'{self.name}s age is {self.age}'