import re

정규표현식 = r'([a-zA-Z]+) : (\d+)'
문자열 = 'name : leehojun, age: 10, height: 180, email: paul-lab@naver.com'
결과 = re.search(정규표현식, 문자열)

print(f're.search(정규표현식, 문자열) : {결과}')

if 결과:
  print(f'결과값의 시작과 끝 : {결과.start()}, {결과.end()}')
  print(f'매칭 그룹핑: {결과.group(0)}')
else:
  print('매칭 결과 없음')