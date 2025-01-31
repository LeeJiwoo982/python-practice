# 기존 방식
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2) # 리스트값추가가

print(squared_numbers)


# 리스트 컴프리헨션
squared_numbers2 = [num **2 for num in numbers]
squared_numbers3 = list(num **2 for num in numbers)
print(squared_numbers2)
print(squared_numbers3)
#반복을 하며 리스트 만들어야 할 때, 축약해서 빠르고 간단하게 제작 가능


#### List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"####
data1 = [[0] * (5) for _ in range(5)]
print(data1)

# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]
print(data2)

"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""


# 리스트 컴프리헨션 with 조건문
# 기존 방식
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# 리스트 컴프리헨션, 가독성 별로, 효율적이고 간결한 것의 단점점
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
