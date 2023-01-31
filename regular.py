# fruits = ['apple','guava','grapes','banana','orange']
# fruits[1:3] = ['watermelon']  # keep in list
# print(fruits)
# output should be ['apple','watermelon','banana','ornage']
# if 'guava' and 'grapes' in fruits:
#     pos = fruits.index('guava')
#     fruits[pos:pos + 1] = 'watermelon'
#     print(fruits)
# else:
#     pass

# fruits[2]='watermelon'
# fruits[1]='watermelon'
# print(fruits)

# def function():
#     def wel_func():
#         print('okay')
#     return wel_func()

# fun = function()
# fun

# def welcome():
#     def welcome_function():
#         print("world hello")
#     return welcome_function()

# var=welcome
# var()


# def any_function():
#     def yo_function():
#         print('river in the moon')
#     return yo_function

# out=any_function()
# out()

# def main_function():
#     def pani_function(x):
#         print(f'hula {x}')
#     return pani_function

# out=main_function()
# out(5)


# def first(name):
#     print(f"{name} inside ship")

# def second(name):
#     print(f'{name} inside poop')

# def greet(func):
#     func('ram')
    
# greet(first)


# def decorator_function(func):
#     def wrapper():
#         print('hello world')
#         func()
#         print('bye everyone')
#     return wrapper
        

# def welcome():
#     print(f'welcome everyone')
    
# w=decorator_function(welcome)
# w()


# def laptop(func):
#     def wrapper():
#         var = func()
#         print(var)
#         return 'mouse'
#     return wrapper

# @laptop
# def welcome():
#     return 'okay'
# print(welcome())

# w=laptop(welcome
# w()



# =================must_know=============
# def myfunction(func):
#     def wrapper():
#         var = func()
#         print(var)
#         return 'done'
#     return wrapper

# @myfunction
# def example():
#     return 'okay'

# print(example())
    
    
    
# profile = {
#     'name':'ram',
#     'gender':'Male',
#     'education':[
#         {'college':'abc college','level':'+2'},
#         {'college':'xyz college','level':'bachelor'},
#     ],
#     'address':[
#         {
#             'temporary':{
#             'ward':1,
#             'city':'kathmandu',
#             },
#             'permanment':{
#             'ward':2,
#             'city':'kavre'
#             }
#         }
#     ]
# }

# print(f'name:{profile.get("name")}')
# print(f'gender:{profile.get("gender")}')
# education = profile.get('education')
# for i in education:
#     print(f"college:{i.get('college')} and level:{i.get('level')}")
    
# address = profile.get('address')
# for i in address:
#     tem = i.get('temporary')
#     print('temporary')
#     for key,value in tem.items():
        
        
#         print(key,":",value)
#     per = i.get('permanment')
#     print('parmanent')
#     for key,value in per.items():
#         print(key,":",value)
#     for kakey,value in i.items():
#     print(f"address:{i.get('temporary')}\nward:{i.get('ward')}\ncity:{i.get('city')} ")
    
# students = {
#     "count": 2,
#     "data": [
#         {
#             "name": "Ram",
#             "address": "Tinknune",
#             "course": "Python Django",
#             "attendance": [
#                 {
#                     "month": "January",
#                     "total_working_days": 25,
#                     "present": 24,
#                     "absent": 1,
#                     "leave": 0,
#                 },
#                 {
#                     "month": "February",
#                     "total_working_days": 28,
#                     "present": 20,
#                     "absent": 2,
#                     "leave": 6,
#                 }
#             ]
#         },
#         {
#             "name": "Hari",
#             "address": "Tinknune",
#             "course": "Python Django",
#             "attendance": [
#                 {
#                     "month": "January",
#                     "total_working_days": 25,
#                     "present": 23,
#                     "absent": 1,
#                     "leave": 1,
#                 },
#                 {
#                     "month": "February",
#                     "total_working_days": 28,
#                     "present": 27,
#                     "absent": 0,
#                     "leave": 1,
#                 }
#             ]
#         }
#     ]
# }

# print(f'count:{students.get("count")}')
# data=students.get('data')
# for i in data:
#     print(f'name:{i.get("name")}')
#     print(f'address:{i.get("address")}')
#     print(f'course:{i.get("course")}')
#     for d in i.get('attendance'):
#         for key,value in d.items():
#              print(f'{key}:{value}')

# user=10
# empty=[]
# for i in range(1,user+1):
#     temp=i+1
#     print(i+temp)

