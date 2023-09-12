num = int(input('숫자를 입력하세요'))
def divisor(num):
  data  = []
  for i in range(1, num+1):
    if num % i == 0:
      data.append(i)
  return data


print(divisor(num))