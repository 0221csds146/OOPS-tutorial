class Employee:
    #Magic method/dunder method/special method
    def __init__(self):#constructor method
        self.id=123
        self.salary = 100000
        self.designation="Software Engineer"
    def travel(self,destination):
        print(f"Travelling to {destination}")

#creating an object of Employee class
sam=Employee()
print(sam.id)
print(sam.salary)
sam.travel("Delhi")
print(type(sam))