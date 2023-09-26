def solution(start_num, end_num):
  result = []
  for i in range(start_num, end_num+1):
    result.append(i)
  return result

solution(3,10)


# 다른 방법

def solution(start_num, end_num):
  st, end = start_num, end_num
  return [i for i in range(st, end+1)]

solution(3,10)