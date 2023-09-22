def repeat(반복자):
  if 반복자:
    while True:
      for 반복자개별요소 in 반복자:
        yield 반복자개별요소
        
def repeat(반복자):
  if 반복자:
    while True:
      for 반복자개별요소 in 반복자:
        yield 반복자개별요소

list(zip('111222333', repeat(['abcd'])))