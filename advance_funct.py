def greet():
    print('hello students')
    print('welcome students')

c = greet                 # call by reference 
c()


def addition(num1,num2):
    print(num1+num2)
    
add = addition
add(12,23)

def outer():  #global scope
    def inner():   #local scope
        print('i am inner function')
    inner()

outer()


# ================this code is wrong
# def calculator():
#     def addition(num1,num2):
#         print(num1+num2)
#     return addition

# add = calculator()
# add(1,2)
# =================this code inside this is wrong




# def calculator(operator):
#     def addition(a,b):
#         return a+b
#     def difference(a,b):
#         return a-b
#     def product(a,b):
#         return a*b
#     if operator == '+':
#         return addition
#     elif operator=='-':
#         return difference
#     elif operator=='*':
#         return product
    
# a = calculator(input(':'))
# print(a(12,10))



# #=====================closure_method=======================
# def increament(num):
#     def factor(val):
#         return num+val
#     return factor

# increase_by = increament(20)
# print(increase_by(10))
# print(increase_by(20))

    
# def main_function():
#     def sec_function(val):
#         print(val%2==0)
#     return sec_function

# inc = main_function()
# inc(20)





# #=====================
# def welcome(name):
#     print(f'welcome {name}')
    
# def bye_bye(name):
#     print(f'bye bye {name}')
    
# def greet(func):
#     func('ram')
   
# greet(welcome) 

# ======================



# ===============without decorator function========

# def decorator_function(func):
#     def wrapper():
#         print('hello every!')
#         func()
#         print('bye everyone@')
#     return wrapper

# def welcome():
#     print(f'welcome everyone')

# w = decorator_function(welcome)
# w()






# ==============decorator function================
# def decorator_function(func):
#     def wrapper():
#         print('hello every!')
#         func()
#         print('bye everyone@')
#     return wrapper

# @decorator_function
# def welcome():
#     print(f'welcome everyone')
# welcome()  # call welcome() if decorator is applied 

# # w = decorator_function(welcome)
# # w()


# import time

# start = time.time()
# total = 0
# for i in range(1000000):
#     total+=i
# print(total)
# stop = time.time()

# print(stop-start)




# import time
# def smart_division(func):
#     def wrapper(a,b):
#         if b==0:
#             return 'could not divide by zero'
#         else:
#             return func(a,b)
#     return wrapper

# start = time.time()
# @smart_division
# def division(a,b):
#     return a/b

# stop = time.time()

# print(division(20,10))
# print(division(20,0))
# print(stop-start)


# import time


# def definition(func):
#     def wrapper():
#         start = time.time()
#         func()
#         var = func()
#         stop = time.time()
#         print(stop-start)
#     return wrapper

# @definition
# def example():
#     total = 0
#     for i in range(100000):
#         total+=i


# example()


# def greet_function():
#     def wrapper():
#         print("okay")
#     return wrapper

# out=greet_function
# print(out())


import time
def welcome(func):
    def wrapper(*a,**k):
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return wrapper
  
@welcome
def example():
    print('hello everyone')

@welcome
def example2(n):
    print(f'{n} times')
    
@welcome
def example3(y = 10,x = 20):
    print(x+y)
    
example()
example2(10)
example3(y=10,x=20)

    