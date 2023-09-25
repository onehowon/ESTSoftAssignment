def solution(a,b):
  c = str(a) + str(b)
  d = str(b) + str(a)
  answer = max(list([int(c), int(d)]))
  return answer

solution(91, 9)