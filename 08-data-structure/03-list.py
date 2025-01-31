# 매우 중요
# 추가와 삭제 관련

# append(x) : list 마지막에 항목 x를 추가
## 원본이 바뀐다. 그래서 str과 구성이 다름. 가변형이라
my_list = [1, 2, 3]
my_list.append(4) 
print(my_list)  # [1, 2, 3, 4] 
print(my_list.append(4))  # None 메서드 자체는 결과값이 없음. 원본수정이라

# extend(iterable) : 리스트에 다른 반복가능한 객체의 모든 항목 추가. 여러개용용
my_list = [1, 2, 3]
my_list.extend([4,5,6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
# print(my_list.extend([4,5,6])) # None

# append와의 비교
my_list.append([4,5,6])
print(my_list) # [1, 2, 3, 4, 5, 6, [4, 5, 6]]
# my_list.extend(9) 
# print(my_list) # error 인트는 iterable이 아니다

# insert(i, x) : 리스트의 지정한 인덱스 위치에 항목 삽입
my_list = [1, 2, 3]
my_list.insert(1, 5) # my_list[1]에 5를 추가

print(my_list)  # [1, 5, 2, 3]

# remove(x) : 리스트에서 x와 첫 번째로 일치하는 항목 삭제
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2) # 처음 나오는 2 삭제
print(my_list)  # [1, 3, 2, 2, 2] 

# pop(i) : 지정한 인덱스 항목 제거하고 반환, 작성하지 않으면 마지막 항목 제거하고 반환
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4] 


# clear() : 모든 항목 삭제
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []


# list 탐색 및 정렬
# index(x) : 첫 번째로 일치하는 항목의 인덱스 반환
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# count(x) : 항목 x의 개수 반환
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3

# reverse() : 순서를 역순으로 변경, 정렬은 아님
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]
print(my_list.reverse())  # None

# sort() : 원본을 오름차순 정렬
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(reverse=True) : 내림차순 정렬
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]

my_list.sort(my_list)
# print(my_list) #TypeError: sort() takes no positional arguments 위치인자없음