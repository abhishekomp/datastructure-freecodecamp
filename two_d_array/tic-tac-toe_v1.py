class Player:
  def __init__(self, name, identifier):
    identifiers = ['x','0']
    self.name = name
    self.identifier = identifier
  
  def __str__(self):
    print(f"Name: {self.name}, Symbol: {self.identifier}")

class TicTacToe:
  def __init__(self):
    self.matrix = self.generateMatrix(3,3)
    self.display_matrix(self.matrix)

  
  def generateMatrix(self, row, col):
    # Fill all the positions using *
    # Assume that row and col are positive integer <=3
    matrix = []    
    for i in range(row):
      l = []
      for j in range(col):
        l.append('*')
      matrix.append(l)
    return matrix

  def display_matrix(self, matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        print(f"'{matrix[i][j]}'", end=" ")
      print("\n")
  
  def play(self):
    player1Name = input("Type 1st player name: ")
    player1 = Player(player1Name)
    player2Name = input("Type 2nd player name: ")
    player2 = Player(player2Name)
    

game = TicTacToe()
game.play()