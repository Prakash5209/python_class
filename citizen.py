# print(list(map(lambda x:x**2,[i for i in range(10)])))
# print(list(filter(lambda x:x%2==0,[i for i in range(10)])))
# lst='what kinds of human is called animal'.split(' ')
# print(list(filter(lambda x:x.startswith('w'),lst)))

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname 
#         self.lastname = lastname 
        
#     def myfunc(self):
#         return f'{self.firstname}:{self.lastname}'
    
# obj = Person('prakash','chaudhary')
# print(obj.myfunc())


class Object:
    def __init__(self,name,planet):
        self.name = name
        self.planet = planet
    
    def printer(self):
        print(self.name,self.planet)
        


class Student(Object):
    def __init__(self,name,planet):
        Object.__init__(self,name,planet)

stu = Student('okay','this')
stu.printer()