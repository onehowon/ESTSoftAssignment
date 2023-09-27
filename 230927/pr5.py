# 7번 카카오 공채문제 5번 난이도 중
# 다중 집합을 허락하지 않았을 때 (일반 집합으로 풀었을 때)
import re

def solution(str1, str2):
  str1=str1.lower()
  str2=str2.lower()

  str1List = []
  str2List = []

  패턴 = re.compile(r'[a-z]{2}')

  for i in range(len(str1)-1):
    문자열 = str1[i]+str1[i+1]
    if 패턴.findall(문자열):
      str1List.append(문자열)

  for i in range(len(str2)-1):
    문자열 = str2[i]+str2[i+1]
    if 패턴.findall(문자열):
      str2List.append(문자열)

  print(str1List, str2List)
  교집합 = set(str1List) & set(str2List)
  합집합 = set(str1List) | set(str2List)

  교집합추가수 = 0

  for i in 교집합:
    if str1List.count(i) > 1 and str2List.count(i) > 1:
      if str1List.count(i) > str2List.count(i):
        교집합추가수 += str2List.count(i)-1
      else:
        교집합추가수 += str1List.count(i)-1

    print(f'교집합추가수는 {교집합추가수}입니다.')
    

  합집합추가수 = 0

  for i in 합집합:
    if str1List.count(i) > 1 and str2List.count(i) > 1:
      if str1List.count(i) > str2List.count(i):
        합집합추가수 += str1List.count(i)-1
      else:
        합집합추가수 += str2List.count(i)-1

    print(f'합집합추가수는 {합집합추가수}입니다.')

  return int((len(교집합) + 교집합추가수) / (len(합집합) + 합집합추가수) * 65536)

testcase = [
    ('FRANCE', 'french'),
    ('handshake', 'shake hands'),
    ('aa1+aa2', 'AAAA12')
]

# 올림은 ceil, 반올림은 round
for str1, str2 in testcase:
  print(solution(str1, str2))
  

# ㅈㄴ 어렵네;