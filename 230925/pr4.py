# 문제3: (class 쓰레드) 사용자로부터 인덱스 값을 입력 받아서 리스트 ["apple", "banana", "cherry"]에서 해당 인덱스의 값을 출력하는 함수를 작성하세요. 사용자가 범위를 벗어난 인덱스를 입력하면 "리스트의 범위를 벗어났습니다."라는 메시지를 출력하세요.

fruit = ["apple", "banana", "cherry"]
class OutOfList(Exception):
  def __init__(self):
    super().__init__('리스트의 범위를 벗어났습니다.')

def choice():

  while True:
    try:
      index = int(input("정수를 입력해주세요: "))
      break
    except:
      print('"다시 입력해주세요"')

    if len(fruit) < index:
      raise OutOfList

    print(fruit[index-1])

choice()