# def welcome():
#     print('welcome to the command prompt')

# welcome()

# def welcome(name,address):
#     print('welcome',name)
#     print('address',address)
    
# name = input('enter your name ')
# address = input('enter your address:')
# welcome(name,address)

# a = 10
# b = 20
# total = a + b
# print('the sum of {} and {} is {}'.format(a,b,total))
# print(f'the sum of {a} and {b} is {total}')

# def profile(name,address,contact):
#     print(f'name:{name}')
#     print(f'address: {address}')
#     print(f'contact: {contact}')

# profile('ra','ktm','123') #position arguments    
# profile(contact='12312',name='hari',address='lalitpur')  # keyword agruments

# def addition(num1,num2 = 2):  # num1 value is default
#     print(num1+num2)
# addition(10)  # return num1  only 
# addition(10,5)  # return mum1 and num2 users give value

# def addition(a,b):
#     print(a + b)
    
# def product(a,b):
#     return a*b

# add = addition(1,2)
# print(add)
# print(f'addition: {add}')

# mul = product(10,5)
# print(f'product: {mul}')

# def multiple_arguments(*a):  # *a = take multiple arguement and store them in tuple
#     print(a)
    
# multiple_arguments(1,2,3,4,'computer','laptop')



# small task  -------------------------------------------


# main = []
# even = []
# odd  = []
# duplicate = []

# def storage(user_input):
#     main.append(user_input)
#     if user_input%2==0:
#         if user_input not in even:
#             even.append(user_input)
#         else:
#             duplicate.append(user_input)
#     else:
#         if user_input not in odd:
#             odd.append(user_input)
#         else:
#             duplicate.append(user_input)
     
# for i in range(15):
#     storage(int(input('enter number:')))

# print(main)
# print(even)
# print(odd)
# print(duplicate)



# for i in range(15):
#     user_input = int(input(':'))
#     main.append(user_input)
#     if user_input%2==0:
#         if user_input not in even:
#             even.append(user_input)
#         else:
#             duplicate.append(user_input)
#     elif user_input%2!=0:
#         if user_input not in odd:
#             odd.append(user_input)
#         else:
#             duplicate.append(user_input)
    
    
# def myfun(x):
#     main.append(x)
#     if x%2==0:
#         even.append(x) if x not in even else duplicate.append(x)
#     elif x%2!=0:
#         odd.append(x) if x not in odd else duplicate.append(x)
        
        
# sir method 



# for i in range(15):
#     num = int(input('enter a number'))
#     if num in main:
#         duplicate.append(num)
#     else:
#         if num%2==0:
#             even.append(num)
#         else:
#             odd.append(num)
#     main.append(num)
    
# print(f'main:{main}\neven:{even}\nodd:{odd}\nduplicate:{duplicate}')


# def multiple_keyword(k):
#     print(k)
    
# def dict_function(**k):
#     for i,j in k.items():
#         print(i,j)
    
# dict_function(name='ram',contact='12323',address='ktm')
