# print(list(map(lambda x:x**2,[i for i in range(10)])))
# print(list(filter(lambda x:x%2==0,[i for i in range(10)])))
# lst='what kinds of human is called animal'.split(' ')
# print(list(filter(lambda x:x.startswith('w'),lst)))


class person:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def person_function(self,name):
        print(self.name)

cal = person('nepal','earth')
cal.name
