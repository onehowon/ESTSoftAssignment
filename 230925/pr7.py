# 정수 a,d, 길이가 n인 boolean 배열 included
# 첫째항 a, 공차 d 등차수열
# included[i] = i+1항
# 1항부터 n항까지 included가 true인 항들만 더한 값을 return
def solution(a,d, included):
  result = 0
  include = []
  for i in included:
    include.append(i)

  for i in range(len(included)):
    if included[i] == True:
      result += a+ (b*i)
  return result

solution(7,1, [False, False, False, True, False, False, False])