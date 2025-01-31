# 문자열을 찾거나 확인
# find('x') : x의 첫번째 위치 반환 없으면 -1
text = 'banana'
print(text.find('x')) # -1
print(text.find('a')) # 1

# index('x') : x의 첫번째 위치 반환, 없으면 error 발생, 코드중단, 해결
print(text.index('a')) # 1
# print(text.index('x')) # 코드 중단 # ValueError: substring not found

# isupper() : 문자열이 전부 대문자인지 체크
# is로 시작하는 내장함수, 메서드는 반환값이 Boolean으로 구성
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower() : 문자열이 전부 소문자인지 체크
print(string1.islower())  # False
print(string2.islower())  # False

# isalpha() : 문자열이 알파벳으로만 이루어져 있는지
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False

# 문자열 조작: 불변의 타입이기에 새 문자열을 반환
# replace(old, new[,count]) : 바꿀 대상 글자를 새로운 객체에 할당해서 바꿔서 반환
## [,count]: 대괄호는 선택적 인자, 바꿀 개수를 지정, 기술문서 작성 시 문법
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
print(text) # Hello, world! world world
 
# strip([chars]) : 문자열과 시작과 끝에 있는 공백 혹은 지정한 문자 제거
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # Hello, world!

# split(sep=None, maxsplit=-1) : sep를 구분자 문자열로 사용하여, 문자열 안에 있는 단어들의 리스트를 반환
text = 'Hello, world!'
words1 = text.split(',') # 구분자를 기준으로 공백은 남아있음
words2 = text.split() # sep을 안쓰면 공백기준
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']


# 'separator'.join(iterable) : iterable의 문자열을 연결한 문자열을 반환
## .join앞에 붙는 거에는 str만 와야함. int오면 error
words = ['Hello', 'world!']
new_text = '-'.join(words) # 리스트의 문자 요소를 연결하는 메서드
new_text2 = ''.join(words) # 없으면 걍 붙는
print(new_text)  # Hello-world!
print(new_text2) # Helloworld!

# capitalize() : 가장 첫번째 글자를 대문자로 변경
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title() : 문자열 내 띄어쓰기 기준으로 각 단어 첫 글자는 대문자로, 나머지는 소문자로
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
