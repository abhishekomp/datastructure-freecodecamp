def generateMatrix(row, col):
    # Fill all the positions using *
    # Assume that row and col are positive integer <=3
    matrix = []    
    for i in range(row):
      l = []
      for j in range(col):
        l.append('*')
      matrix.append(l)
    return matrix

def display_matrix(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        print(f"'{matrix[i][j]}'", end=" ")
      print("\n")

def play():
   matrix = generateMatrix(3, 3)
   display_matrix(matrix)
  
if __name__ == '__main__':
   play()