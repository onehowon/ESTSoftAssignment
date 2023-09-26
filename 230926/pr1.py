def solution(numLog):
  result=''
  for i in range(len(numLog) -1):
    if numLog[i+1] - numLog[i] == 1:
      result += 'w'
    if numLog[i+1] - numLog[i] == -1:
      result += 's'
    if numLog[i+1] - numLog[i] == 10:
      result += 'd'
    if numLog[i+1] - numLog[i] == -10:
      result += 'a'
  return result

solution([0,1,0,10,0,1,0,10,0,-1,-2,-1])

# 또 다른 방법
def solution(numLog):
  keyboard = dict(zip([1, -1, 10, -10], ['w','s','d','a']))
  print(keyboard)
  result = ''
  for num in numLog:
    result += str(keyboard.get(num, 0))
    print(keyboard.get(num))
  return result

solution([0,1,0,10,0,1,0,10,0,-1,-2,-1])