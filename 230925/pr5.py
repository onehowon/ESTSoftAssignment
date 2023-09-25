def fib(n):
  fibolist = []

  if n == 1:
    fibolist.append(1)
    return fibolist
  if n == 2:
    fibolist.append(1)
    fibolist.append(1)
    return fibolist

  a,b = 1, 1
  fibolist = [1, 1]
  for i in range(n-2):
    c = a+b
    fibolist.append(c)
    a=b
    b=c
  return fibolist

print(fib(5))