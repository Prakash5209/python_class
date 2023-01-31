# map and filter 
# lambda 


# a = lambda x,y:x*y
# print(a(10,20))

# map(func, iterable_object)

# a=[2,9,8,17,15,90]

# def increase_by_one(n):
#     return n+1

# output = list(map(increase_by_one,a))
# print(output)

name_list=['ram','shayam','sita','meera','heri']
# output = lambda x:x.capitalize()
# print(list(map(output,name_list)))


# print(list(map(lambda x:x.capitalize(),name_list)))

# lst = [i for i in range(10)]
# out=list(filter(lambda x:x%2==0,lst))

# print(out)

# a='2,4,6,d,8,9,e,4'
# b = a.split(',')
# numb = filter(str.isdigit,b)
# print(list(numb))
# print(sum(map(int,numb)))


# out = lambda x:x.isdigit()
# c = list(map(out,b))
# print(c)

# print(sum(map(int,filter(str.isdigit,a.split(',')))))

marks_of_students=[
    {
        'name':'ram',
        'marks':{'maths':80,'science':85,'computer':90}
    },
    {
        'name':'sita',
        'marks':{'maths':87,'science':79,'computer':85}
    },
    {
        'name':'hari',
        'marks':{'maths':90,'science':75,'computer':88}
    }
]
em = []
for i in marks_of_students:
    marks = i.get('marks')
    math = marks.get('maths')
    science = marks.get('science')
    computer = marks.get('computer')
    lst=[math,science,computer]
    num = sum(lst)
    high = f"{i.get('name')}:{sum(lst)}"
    em.append(num)
    
print(sorted(em))
print(sorted(em)[-1])
em = []
for i in marks_of_students:
    lst=[i.get('name'),sum(i.get('marks').values())]
    em.append(lst)

output=list(reversed(sorted(em,key=lambda x:x[1])))
pos=['first','second','third']

