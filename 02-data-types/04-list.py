# 리스트 표현
my_list_1 = [] # 빈리스트 생성
my_list_2 = [1, 'a', 3.4, 'b', 5] # 정수, 실수, 문자열 가능
my_list_3 = [1, 2, 3, 'python', ['hello','world']] # 리스트 안에 리스트
my_list = [1, 'a', 3, 'b', 5]

# 인덱싱
print(my_list[1])  # a

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1], 뒤집기, 정렬(내림차순)아님

# 길이
print(len(my_list))  # 5

# 중첩된 리스트 접근
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))  # 5 리스트 안의 요소를 세는 것
print(len(my_list[3])) # 6
print(my_list[4][2])  # !!! # 해결~ [4][-1]
print(my_list[4][1][0])  # w 해결

# 리스트는 가변
my_list = [1, 2, 3]
my_list[0] = 100
my_list_test = [1, 'world', 3]
my_list_test[1] =100 # 문자열을 바꾼게 아니라, 요소를 변경, 재할당 아님님
print(my_list_test)