from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 3)

def random_col(board):
  return randint(0, len(board[0]) - 1)
row = random_row(board)
ship_row=[row, row+1, row+2]
col = random_col(board)
ship_col= [col]

print ship_row, ship_col

turn = 0
hit_count = 0
while turn < 5:
  print "Turn", turn +1
  guess_row = int(raw_input("Guess Row: "))-1
  guess_col = int(raw_input("Guess Col: "))-1
  if guess_row in ship_row and guess_col in ship_col and board[guess_row][guess_col] == "O":
    print "Hit!"
    hit_count+=1
    board[guess_row][guess_col] = "H"
    if hit_count==3:
      print_board(board)
      print "Congratulations, you sunk my battleship!"
      break
    else:
    	print_board(board)
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "H"):
      print "You guessed that one already."
    else:
      turn += 1
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      print_board(board)
else:
  print "Game Over, You Lose!"