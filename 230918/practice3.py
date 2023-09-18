import re

정규표현식 = r'^[1-9]1010[0-5]{2}0$'
문자열 = '71010330'
결과 = re.findall(정규표현식, 문자열)

if 결과:
  print('Yes')
else:
  print('No')