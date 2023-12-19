import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

    
def is_board_full(board):
     return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
     return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
     if check_winner(board, '0'):
          return -1
     elif check_winner(board, 'X'):
          return 1
     elif is_board_full(board):
          return 0

     if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
     else:
          min_eval = float('inf')
          for i, j in get_empty_cells(board):
               board[i][j] = '0'
               eval = minimax(board, depth + 1, True)
               board[i][j] = ' '
               min_eval = min(min_eval, eval)
          return min_eval
     
def get_best_move(board):
     best_move = None
     best_eval = float('-inf')

     for i, j in get_empty_cells(board):
          board[i][j] = 'X'
          eval = minimax(board, 0, False)
          board[i][j] = ' '

          if eval > best_eval:
               best_eval = eval
               best_move = (i, j)

          return best_move
     
def play_tic_tac_toe():
     board = [[' ' for _ in range(3)] for _ in range(3)]
     player_turn = True

     while True:
          print_board(board)

          if player_turn:
               row = int(input("Enter the row (0, 1, or 2): "))
               col = int(input("Enter the column (0, 1, or 2): "))

               if board[row][col] == ' ':
                    board[row][col] = '0'
                    player_turn = not player_turn
               else:
                    print("Cell already occupied. Try again")
                    continue
          else:
               print("AI is thinking..")
               ai_move = get_best_move(board)
               board[ai_move[0]][ai_move[1]] = 'X'
               player_turn = not player_turn

          if check_winner(board, '0'):
               print_board(board)
               print("Congrats! You won!")
               break
          elif check_winner(board, 'X'):
               print_board(board)
               print("The AI won!")
               break
          elif is_board_full(board):
               print_board(board)
               print("Its a draw")
               break

if __name__ == '__main__':
     play_tic_tac_toe()
