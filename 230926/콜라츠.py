# x 짝수 -> / 2 , x 홀수 -> 3*x+1 언제 반드시 x가 1? 1000보다 작거나 같은 수
def solution(x):
  result = x
  arr1 = [x]
  while True:
    if result == 1:
      break
    if result % 2 == 0:
      result = result / 2
      arr1.append(int(result))
    if result == 1:
      break
    if result % 2 == 1:
      result = (result*3)+1
      arr1.append(int(result))
  return arr1

solution(586)