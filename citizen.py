# print(list(map(lambda x:x**2,[i for i in range(10)])))
# print(list(filter(lambda x:x%2==0,[i for i in range(10)])))
# lst='what kinds of human is called animal'.split(' ')
# print(list(filter(lambda x:x.startswith('w'),lst)))


lst = [i for i in range(10)]
print(list(map(lambda x:x*2,filter(lambda x:x %2 == 0,lst))))