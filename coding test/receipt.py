X = int(input()) # 총 금액
N = int(input()) # 물건 종류의 수

shop_list = []
for i in range(1, N+1):
  price, pair = map(int, input().strip().split())
  shop_list.append(price*pair)
  a = sum(shop_list)
if a == X:
  print('Yes')
else:
  print('No')