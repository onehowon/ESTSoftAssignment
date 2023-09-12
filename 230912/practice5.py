def solution(l):
  return sorted(l, key=lambda x: x[1], reverse=True)

solution([[10,5],[20,3], [30,4], [40, 1]])