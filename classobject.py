# # Objects oriented programming

# # Class and object
# # Encapsulation
# # Inheritance
# # Polymorphism
# # Abstraction


# class Projector:
#     def __init__(self,color,year,model):
#         self.color=color
#         self.year=year
#         self.model=model
        
#     def visualise(self):
#         print(f"projector of model {self.model} is visualising")
    
#     def description(self):
#         print(f'color:{self.color}')
#         print(f'model:{self.model}')
#         print(f'year:{self.year}')
        
#     def __str__(self):
#         return self.color
    
#     def __repr__(self):
#         return f"{self.color} - {self.year}"
#     # def function(self):
#     #     print(f'this is color :{self.color}')
        
# p1=Projector('white',1232,'sdf123')
# p2=Projector('red',2434,'sdkfj65')

# print('okay')
# # print(p1.__repr__)
# print(p2)
# print(p1.__dict__)
# print(p2.__dict__)

# # p1.visualise()        
# # p2.visualise()

# # # p1.description()
# # p2.description()
# # p2.function()

# # output=Projector('white',2323,"NEC")
# # print(output.color)
# # print(output.year)
# # print(output.model)





# projectors=[]
# for i in range(2):
#     color=input('color:')
#     year=input('year:')
#     model=input('model:')
#     p=Projector(color,year,model)
#     projectors.append(p)
    

# print(projectors)






# whole new stage-------------------------------------------------

# class Student:
#     def __init__(self,_id,name,contact,address):
#         self._id=_id
#         self.name=name
#         self.contact=contact
#         self.address=address
#         self.total_attendance=0

#     def update_attendance(self):
#         self.total_attendance+=1
        
#     def view_attendance(self):
#         return self.total_attendance
    
# s=Student(1,'ram','1313','ktm')
# s2=Student(2,'shyam','3434','bkt')

# s.update_attendance()
# s2.update_attendance()
# s2.update_attendance()

# print(s.view_attendance())
# print(s2.view_attendance())

# print(Student.view_attendance(s))
    
# complete whole new state ----------------------------------------------






# next stage --------------------------


# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.__price=price
        
#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,price):
#         if price>0:
#             self.__price=price
    
# tshirt=Product("tshit",500)
# jacket=Product('jacket',1000)

# print(f'before setting: {tshirt.price}')
# tshirt.price=1
# print(f'after settings: {tshirt.price}')





# another one------------------
# class Calculator:
#     def __init__(self,num1,num2):
#         self.a=num1
#         self.b=num2
    
#     def add(self):
#         return self.a+self.b
    
#     def difference(self):
#         return self.a-self.b
    
#     def product(self):
#         return self.a*self.b
    
#     def division(self):
#         return self.a/self.b
    
#     @staticmethod 
#     def square_root(num):
#         return num**0.5


# s=Calculator(5,5)
# # print(c.add())
# print(Calculator.square_root(5))  





# next stage-------------------------------------------
# class or staticmethod variable method


# class Student:
#     college="abc college" 
    
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
    
# print(Student.college)
# s=Student('ram','345345')
# print(s.college)
# print(s.__dict__)


# class User:
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
    
#     @classmethod
#     def create_user_with_random_password(cls,username):
#         return cls(username,"Default_password")
    
# u=User('ram@gmail.com','demo1234')
# print(u.__dict__)

# u2=User.create_user_with_random_password('hari@gmail.com')
# print(u2.__dict__)
    



# w3school.com classes and objects

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname 
#         self.lastname = lastname
        
#     def __str__(self):
#         return f'{self.firstname}:{self.lastname}'
    
# p1 = Person('earth','other')
# print(p1)




# object method ↓

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
        
#     def myfunction(self):
#         return f'{self.firstname}:{self.lastname}'
    
# p1 = Person('prakash','chaudhary')
# print(p1.myfunction())