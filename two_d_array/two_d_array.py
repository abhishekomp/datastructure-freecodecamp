

def iterate_over_2d_array():
  arr_2d = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
  for row in arr_2d:
    for item in row:
      print(item)

def iterate_over_2d_array_method2():
  arr_2d = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
  for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
      #print(arr_2d[i][j], end=" ")
      print(f"'{arr_2d[i][j]}'", end=" ")
    print("\n")
  
  

if __name__ == '__main__':
  #iterate_over_2d_array()
  iterate_over_2d_array_method2()