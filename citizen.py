def decorator_function(func):
    def primary():
        print('okay world')
        func()
        print('always last')
    return primary
        

@decorator_function
def welcome():
    print('i am always in the middle')

welcome()
# variable=decorator_function(welcome)
# variable()