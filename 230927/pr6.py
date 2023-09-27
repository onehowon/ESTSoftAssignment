# 7번 카카오 공채문제 5번 난이도 중
# 다중 집합을 허락하지 않았을 때 (일반 집합으로 풀었을 때)
import re

def solution(str1, str2):
  str1=str1.lower()
  str2=str2.lower() # 소문자 변환

  str1List = []
  str2List = []

  패턴 = re.compile(r'[a-z]{2}') # 정규표현식(두 문자열에서 2글자씩 묶어서 다중 집합의 원소로 추출)

  for i in range(len(str1)-1): # 두 문자열의 다중집합을 각각 str1list와 str2list에 저장
    문자열 = str1[i]+str1[i+1]
    if 패턴.findall(문자열):
      str1List.append(문자열)

  for i in range(len(str2)-1):
    문자열 = str2[i]+str2[i+1]
    if 패턴.findall(문자열):
      str2List.append(문자열)

  print(str1List, str2List)
  교집합 = set(str1List) & set(str2List) # 교집합 , 합집합을 구할 때는 Python의 set 자료형을 이용
  합집합 = set(str1List) | set(str2List)

  교집합추가수 = 0

  for i in 교집합: # 교집합과 합집합에 대해 추가된 원소 수를 계산. 이를 위해 두 문자열에서 같은 원소가 여러번 나타날 경우 중복횟수를 고려해 추가된 원소 수를 계산
    if str1List.count(i) > 1 or str2List.count(i) > 1:
      if str1List.count(i) > str2List.count(i):
        교집합추가수 += str2List.count(i)-1
      else:
        교집합추가수 += str1List.count(i)-1

    print(f'교집합추가수는 {교집합추가수}입니다.')
    

  합집합추가수 = 0

  for i in 합집합:
    if str1List.count(i) > 1 or str2List.count(i) > 1:
      if str1List.count(i) > str2List.count(i):
        합집합추가수 += str1List.count(i)-1
      else:
        합집합추가수 += str2List.count(i)-1

    print(f'합집합추가수는 {합집합추가수}입니다.')

  return int((len(교집합) + 교집합추가수) / (len(합집합) + 합집합추가수) * 65536) # 유사도를 계산
  # 유사도는 (교집합 크기 + 교집합에 추가된 원소 수) / (합집합 크기 + 합집합에 축된 원소 수)

testcase = [
    ('FRANCE', 'french'), # FRANCE와 french의 경우 유사도가 계산되고 출력됨
    ('handshake', 'shake hands'),
    ('aa1+aa2', 'AAAA12')
]

# 올림은 ceil, 반올림은 round
for str1, str2 in testcase:
  print(solution(str1, str2))