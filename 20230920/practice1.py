def input_num(n):
    for i in range(1, n+1):
        print("O" * (n-1) + ("X" * i))
        
input_num(6)