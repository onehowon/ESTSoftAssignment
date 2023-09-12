def solution(s):
  total = 0
  for char in s:
    if char.isnumeric():
      num = int(char)
      total+=num
  return print(total)

solution('11123')