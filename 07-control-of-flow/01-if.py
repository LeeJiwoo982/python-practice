# a = 3

# if a > 3 :
#     print('3 초과')
# else:
#     print('3 이하')

# print(a)

dust = 35

# 조건문은 순차적으로 진행되고 한 번 걸리면 거기서 끝남
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


# 조건문 중첩가능. 150 초과인데 300도 넘으면
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# >> 매우나쁨\n위험해요!
