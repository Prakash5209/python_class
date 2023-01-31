# inheritance

#child class "IS A" parent class
#Teacher "is a " Person => this is correct
#Dog "IS A " person => this is incorrect

# class Person:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         # self.age=age
        
#     def walk(self):
#         print(f"{self.name} is walking")
        
#     # def person_age(self):
#     #     print(f"{self.age} years old")
        

# class Teacher(Person):
#     def __init__(self,name,address,designation):
#         super().__init__(name,address)
#         self.designation=designation
#         # print(f'{self.designation} okay')
        
#     def teach(self):
#         print(f"{self.name} is teaching")
        

# class Student(Person):
#     def __init__(self,name,address,roll_number):
#         super().__init__(name,address)
#         self.roll=roll_number
    
#     def walk(self):
#         print(f"{self.name} is running")
    
    
# s=Teacher("ram",'ktm')
# s.walk()
# s.teach()
# s.designation

# hi=Student('shyam','ktm','3')
# hi.walk()


# stu=Student('shyam','lalitpur')
# s.person_age()









# next phase---------------------------------

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

class Person(User):
    def __init__(self,username,password,name,address):
        super().__init__(username,password)
        self.name=name
        self.address=address
        
    def profile(self):
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"username: {self.username}")
        
class Student(Person):
    def __init__(self,username,password,name,address,rollno):
        super().__init__(username,password,name,address)
        self.roll_number=rollno
        
    def rollnumber(self):
        print(f"rollno: {self.roll_number}")
        
class Teacher(Person):
    def __init__(self,username,password,name,address,designation):
        super().__init__(username,password,name,address)
        self.designation=designation
    
    def t_designation(self):
        print(f"designatino: {self.designation}")
        
        
per=Person('shyam@','123123','ktm','nex')
per.profile()

print("\n")

stu=Student('ram@','ram123','ram','ktm','123')
stu.profile()
stu.rollnumber()

print("\n")

tec=Teacher('ram@','ram234234','ramayan','lalitpur','4324')
tec.profile()
# tec.rollnumber()
tec.t_designation()
