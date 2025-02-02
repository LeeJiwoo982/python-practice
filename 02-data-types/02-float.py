d = 3.14
e=-2.7

number =314e-2

print(number) # 3.14
print(type(number)) #<class 'float'>

print(2/3) # 0.6666666666666666
print(5/3) # 1.6666666666666667

a=3.2-3.1
b=1.2-1.1

print(a) # 0.10000000000000009
print(b) # 0.09999999999999987
print(a==b) # False

from decimal import Decimal

a=Decimal('3.2')-Decimal('3.1')
b=Decimal('1.2')-Decimal('1.1')
 
print(a) # 0.1 
print(b) # 0.1
print(a==b) # True