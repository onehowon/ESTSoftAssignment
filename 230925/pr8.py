def solution(n, control):
  for i in control:
    if 'w' in i:
      n+=1
    if 's' in i:
      n-=1
    if 'a' in i:
      n-=10
    if 'd' in i:
      n+=10
  return n

solution(0, "wsdawsdassw")
