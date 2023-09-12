def solution(l):
  differ = []
  for sublist in l:
    diff = sublist[0] - sublist[1]
    differ.append(diff)
  return differ

solution([[10,5], [20,3], [30,4], [40,1]])