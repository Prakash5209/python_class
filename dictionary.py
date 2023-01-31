#==================setdefault==============
# b = {}
profile = {'name':'ram','address':'ktm','contact':'12312323'}
# print(profile.setdefault('nam','unknow'))
# profile['nam'] = 'mero nam'



#===================fromkeys===================
# a = ['first','second','address']
# profile = {}
# b = profile.fromkeys(a,'unkown')  # assign 'unkown' value in every single key 
# print(b)
# print(profile.fromkeys(a,'not now'))



#====================items()
# print(profile.items())
# print(profile.keys())
# print(profile.values())

# for i in profile.values():
#     print(i)

# for key,value in profile.items():
#     print(key,value)

# for i in profile.items():       # return values and keys in tuple x   
#     print(i)

# profile.popitem()           #remove last element
# profile.pop('name')      # remove give element
# profile.update({'roll':123})
# profile.update(roll='12')
# profile['verified'] = True
# print(profile)



#===========================
colors = ['yellow','red','orange','blue','violet','red','white']
colors_to_remove = ['red','violet']
new_ary = []
for i in colors:
    if i not in colors_to_remove:
        new_ary.append(i)
        
print(new_ary)

# an = []
# for i in colors:
#     if i in colors_to_remove:
#         an.append(i)
        
# for i in an:
#     colors.remove(i)
# print(colors)


#=============================
        
        
#['yellow','orange','blue','white']


fruits = ['apple','guava','grapes','banana','orange']
# fruits = ['apple','guava','banana','grapes','orange']
# replace 'guava' and 'grapes' with watermelon
# ['apple','watermelon','banana','orange']
