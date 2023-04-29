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
    def __init__(self,assignment):
        self.assignment = assignment
        
    def __str__(self):
        return f'{self.assignment}'
    
    def method(self):
        return f'method {self.assignment}'
    

class Child(Object):
    pass 

sub = Child('earth')
print(sub)
print(sub.method())