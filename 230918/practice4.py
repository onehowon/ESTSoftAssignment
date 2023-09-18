import re

정규표현식 = r'(http|https)://(\w+)(\w+|\.|\-l/)+(:[0-9]+)?'
문자열 = '6746-29301-28391 http://paullab.co.kr:80 064-029-1922 paul-lab@naver.co.kr'
결과 = re.search(정규표현식, 문자열)

결과
결과.group(4)

print(f'프로토콜 : {결과.group(1)}')
print(f'호스트 : {결과.group(2)}')
print(f'포트 : {결과.group(4)[1:]}')