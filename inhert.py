class Animal:
    
    def __init__(self,name):
        self.name=name
        
        
    def speak(self):
        print(f"{self.name} makes sound")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name) #Super() keyword
        self.behaviour="Friendly"
        
    def speak(self): #Method overloading
        super().speak() #Super() keyword
        print(f"{self.name} barks.his behaviour is {self.behaviour}")

#animal=Animal("Biological Animal")
#animal.speak()

dog1=Dog("Sheru")
dog1.speak() #inherting parent class method


