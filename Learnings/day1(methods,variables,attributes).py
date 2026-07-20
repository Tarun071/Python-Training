'''
#types of variables
1.local variable
2.global variable
3.instance variable
4.class variable

#types of attributes 
1.class attribute
2.instance attribute

#types of methods
1.instance method
2.class method
3.static method

'''
class Student:

    college = "Miracle Software Systems" #class variable # class attribute
    def __init__(self,number):
        self.number=number #instance variable #instance attribute

    #insatance method
    def number_dis(self):
        print(self.number) 
    
    #class method
    @classmethod
    def show_college(cls):
        print(cls.college)
        # print(self.number)

    #static method
    @staticmethod
    def branch():
        print("csd")
ob=Student(1) #object
ob.number_dis()
ob.show_college()
Student.branch()
