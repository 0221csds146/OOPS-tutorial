class Animal:
    
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def speak1(self):
        print(f"{self.name} barks")


animal=Animal("Biological Animal")
animal.speak()

dog1=Dog("Buddy")
dog1.speak1()