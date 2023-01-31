# try:
#     # block of code 
# except Exception:
#     # block of code
# except ValueError:
#     # block of code
# except TypeError:
#     # block of code
# else:
#     # block of code
# finally:
#     # block of code 



# try:
#     num1=int(input(':'))
#     num2=int(input(':'))
#     numbers=num1+num2
# except ValueError:
#     print('can not convert to integer')
# else:
#     print(numbers)
    
# name=input('enter your name:')
# print(name)




# making your own error--------------
class ProoductPriceError(Exception):
    pass

class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,price):
        if price<=0:
            raise ProoductPriceError('Price can not be less than zero')
        self.__price=price
    
tshirt=Product("Tshirt",500)

try:
    tshirt.price=-100
    print(f'without exception: {tshirt.price}')
except ProoductPriceError as msg:
    print(msg)
    print(f"after exception {tshirt.price}")