T = int(input())
for i in range(1, T+1):
  A,B = map(int,input().strip().split())
  print(f'Case #{i}: {A} + {B} = {A+B}')