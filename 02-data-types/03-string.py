#문자열ㄹ
print("Hello, World")
print(type('Hello, World'))

print(
    '문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.'
)
print(
    "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
)

print('철수야\'안녕\'')
print('이 다음은 엔터\n입니다.')

bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')

my_str='hello'
# 1. 인덱싱
print(my_str[1])

# 2. 슬라이싱'
#ll
print(my_str[2:4])

#hel
print(my_str[:3])

#lo
print(my_str[3:])

#hlo
print(my_str[::2]) # 0:5:2

#olleh
print(my_str[::-1])

# 길이
print(len(my_str))

# 문자열은 불변
my_str[1]='z'