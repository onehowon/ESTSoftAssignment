# 카카오 2019 1번
def solution(record):
  answer = []
  user = {}

  for log in record:
    logSplit = log.split(' ')
    if logSplit[0] == 'Enter':
      user[logSplit[1]] = logSplit[2]
      answer.append([logSplit[1], '님이 들어왔습니다.'])
    elif logSplit[0] == 'Leave':
      answer.append([logSplit[1], '님이 나갔습니다.'])
    elif logSplit[0] == 'Change':
      user[logSplit[1]] = logSplit[2]
    
  answer = [user[i[0]] + i[1] for i in answer]

  return answer
testcase = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo','Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']

print(solution(testcase))