class Employee:
    
    __user_id=1;# Static attriute

    def __init__(self):#constructor method
        self.__name='Default user'
        self.id=Employee.__user_id
        Employee.__user_id+=1
        self.salary = 100000
        self.designation="Software Engineer"

    # ///geeter and setter method
    @staticmethod
    def get_id():
        return Employee.__user_id
    @staticmethod
    def set_id(value):
        Employee.__user_id=value

    # def get_name(self):
    #     return self.__name  /// Within the class no need to do namemangling(obj._ClassName__name),it provide access within the class
    
    # def set_name(self,value):
    #     self.__name=value
    
    def travel(self,destination):
        print(f"Travelling to {destination}")

#creating an object of Employee class
sam=Employee()
print(sam.id)
sam2=Employee()
print(sam2.id)
print(Employee.get_id())
Employee.set_id(23)
sam3=Employee()
print(sam.id)


# print(sam._Employee__name)
# print(sam.get_name())
# sam.set_name("Rohit")
# print(sam.get_name())
# sam.name="sam kumari"
# print(sam.name)
# print(id(sam))
# print(sam.id)
# print(sam.salary)
# sam.travel("Delhi")
# print(type(sam))