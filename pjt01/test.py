import requests
import pprint

# 하드코딩 한 변수는 대문자로 쓰는 규칙
URL = 'https://fakestoreapi.com/carts' #요청주소
# .get(URL) ; URL 주소에 요청을 보내는 메서드
data = requests.get(URL)
# <Respond [200]>
# [200] ; 웹의 응답코드 -> 정상적으로 응답하였습니다.
# [404] ; not found -> 알 수 없는 주소로 요청했다.
print(data)

# .json() : 데이터를 JSON 형태로 변환해주는 메서드
json_data = data.json()
# print(json_data) #알아보기 어려움 >> import pprint
# print(type(json_data)) # 리스트타입
pprint.pprint(json_data)

