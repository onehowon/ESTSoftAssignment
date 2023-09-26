from collections import Counter
def solution(a,b,c,d):
  arr1 = [a,b,c,d]
  counter = Counter(arr1)
  if len(counter) == 1:
    return 1111 * a
  if len(counter) == 2:
    p,q = counter.keys()
    if counter[p] == 2 and counter[q] == 2:
      return (p+q) * abs(p-q)
    else:
      if counter.get(p) == 3:
        return ( 10 * p + q ) ** 2
      if counter.get(p) == 1:
        return ( 10 * q + p) ** 2
    if len(counter) == 3:
      for key, value in counter.items():
        if value == 1:
          if 'single1' not in locals():
            single1 = key
          else:
            single2 = key
        return single1 * single2
      if len( counter) == 4:
        return min(arr1)
solution(3,2,2,2)