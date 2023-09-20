def div(a,b):
  if b == 0:
    print('0으로 나눌 수 없습니다.')
    return None
  return a/b

result = div(3,0)
if result is not None:
  print("결과:", result)