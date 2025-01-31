# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20

func()

# print('global', num)  # NameError: name 'num' is not defined
# num은 지역변수로 글로벌에서 출력하려해도 이미 함수 안에서만 수명이 다한 변수임.

# 1.local(현재 작업 중), 2.Enclosed(함수안에 함수, 지역 한단계 위)
# , 3.Global(최상단), 4.Built-in(모든 것, 정의않고 사용가능)
# 함수 내 바깥 변수 접근 가능 but 수정 불가능

# sum-내장함수, G에서 sum에 할당하면
# LEGB순으로 찾다가 글로벌에서 찾으면 내장함수 sum으로 사용못하게 됨
# `del sum` 입력 후 진행..이지만 이런 경우를 만들면 안됨됨

# LEGB Rule 퀴즈
a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  # 10(정의에는 없어서 하나 지역 올라가니 있음), 2(글로벌에 있음), 500(밑에서 호출에 넣은 매개변수값에 넣은 게 나온 것) 
        #함수 호출 후 출력

    local(500)
    print(a, b, c)  # 10, 2, 3 # 


enclosed() #여기가 호출부분분

print(a, b)  # 1, 2
