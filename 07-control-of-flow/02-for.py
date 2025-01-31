# 기본 조건문 list
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

# 문자열 순회
country = 'Korea'

for char in country:
    print(char)

#딕셔너리 키와 밸류 뽑기
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict: # key가 튀어나옴. 임시변수 key라 하면 명시적
    print(key)
    print(my_dict[key])

#인덱스 관점 접근=> 알고리즘에 많이 쓴다.
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): # 시퀀스의 길이값으로 돌겠다.
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]

#2중 for문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers: # A> c> d>>B >c > d
    for inner in inners:
        print(outer, inner)
        # 시퀀스 길이만큼 돈다
"""
A c
A d
B c
B d
"""

# 중첩된 리스트에 접근=> 2중 for문
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
