fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits, 3): #인덱스를 3부터 시작가능
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
