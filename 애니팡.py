# 애니팡
def peung(board):
  while(peung_chain(board)):
    filled_board(board)

def peung_chain(board):
  peung_list = []

  flag = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] != 0:
        if j<3 and (board[i][j] == board[i][j+1] == board[i][j+2]):
          flag = 1
          k = j
          while (k<5 and (board[i][j] == board[i][k])):
            peung_list.append((i,k))
            k+=1
        if i<3 and (board[i][j] == board[i+1][j] == board[i+2][j]):
          flag = 1
          k = i
          while (k<5 and (board[i][j] == board[k][j])):
            peung_list.append((k,j))
            k+=1

  for item in peung_list:
    board[item[0]][item[1]] =0

  if flag == 1:
    return True
  else:
    return False

def filled_board(board):
  for i in range(1,5):
    for j in range(5):
      k=i
      while(k>0):
        if board[k][j] == 0 and board[k-1][j] != 0:
          board[k][j] == board[k-1][j]
          board[k-1][j] =0
          k -=1
        else: break


def print_board(board):
  for i in range(5):
    print("{0} {1} {2} {3} {4}".format(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4]))
  print("")

def main():
    board = [[2, 4, 1, 2, 1], [3, 4, 2, 3, 3], [2, 4, 1, 2, 2], [4, 4, 4, 1, 2], [4, 2, 3, 3, 2]]
    peung(board)
    print_board(board)


main()
print(main())
