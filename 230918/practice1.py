from IPython.utils.text import re
import re
문자열 = '[(name, leehojun), (age, 10), (height, 180), (email, paul-lab@naver.com)]'

정규표현식 = r'\((.*?), (.*?)\)'
결과 = re.findall(정규표현식, 문자열)

결과