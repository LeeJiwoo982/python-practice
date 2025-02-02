import requests
from pprint import pprint

#서울의 위도
lat = 37.56
#서울의 경도
lon = 126.97
API_KEY = '735048f25c32203aa27eddf81eaf2a9a' # 상수는 대문자

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

data = requests.get(URL).json()
pprint(data)