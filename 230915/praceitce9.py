import re

정규표현식 = r'([a-zA-Z]+): (\d+)'
문자열 = 'name : leehojun, age : 10, height: 180, email : paul-lab@naver.com'
결과 = re.findall(정규표현식, 문자열)

print(f're.findall(정규표현식, 문자열) : {결과}')