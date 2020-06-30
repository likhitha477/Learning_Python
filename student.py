class student:
    #class variable
    school = 'Telusko'
    def __init__(self,m1,m2,m3):
        #instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    #static method
    @statismethod
    def info():
        print("This is student class in learning python repository.")

s1 = student(32,67,43)
s2 = student(60,30,40)

print(s1.avg()) #instance method
print(student.getSchool()) #class method

student.info()
