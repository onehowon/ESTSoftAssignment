def solution(dartResult):
  패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
  answer = []
  계산식 = {
      'S':lambda 값:값,
      'D':lambda 값:값**2,
      'T':lambda 값:값**3,
  }
  for 숫자, 승수, 상 in 패턴.findall(dartResult):
    if 승수 == 'S':
      점수 = 계산식['S'](int(숫자))
    elif 승수 == 'D':
      점수 = 계산식['D'](int(숫자))
    elif 승수 == 'T':
      점수 = 계산식['T'](int(숫자))
    if 상 == '*':
      점수 *=2
      if answer:
        answer[-1] *=2
    elif 상 == '#':
      점수 *= -1
    answer.append(점수)

  return answer

print(solution('1S2D*#4T'))
