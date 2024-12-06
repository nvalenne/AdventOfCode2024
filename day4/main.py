import re

def get_matrix():
    matrix = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            matrix.append(line.strip())
    f.close()
    return matrix

def match_xmas(matrix, pattern):
    occurences = 0
    for row in matrix:
        row = ''.join(row)
        # Right way + reverse way
        occurences += len(re.findall(pattern, row))
        occurences += len(re.findall(pattern, row[::-1]))
    return occurences

def get_diagonals(matrix):
  diagonals = []
  rows, cols = len(matrix), len(matrix[0])

  # top-right to bottom-left
  for d in range(-(rows - 1), cols):
      diag = [matrix[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
      diagonals.append(diag)

  # top-left to bottom-right
  for d in range(rows + cols - 1):
      diag = [matrix[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))]
      diagonals.append(diag)

  return diagonals

def first_part(matrix):
    pattern = "XMAS"
    num_of_xmas = 0
    
    num_of_xmas += match_xmas(matrix, pattern)
    num_of_xmas += match_xmas(list(zip(*matrix)), pattern)
    num_of_xmas += match_xmas(get_diagonals(matrix), pattern)

    return num_of_xmas

def second_part(matrix):
   patterns = ["MAS", "SAM"]
   xmas = 0
   for i, row in enumerate(matrix):
       for j in range(len(row)):
           if i > 0 and j > 0 and i < len(matrix)-1 and j < len(row)-1:
               # Get diagonals
               left_diag = str(matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1])
               right_diag = str(matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1])
               # Check if it's a X-MAS shape
               if left_diag in patterns and right_diag in patterns:
                   xmas+=1
   return xmas


if __name__ == "__main__":
    matrix = get_matrix()
    print(f"First part: {first_part(matrix)}")
    print(f"Second part: {second_part(matrix)}")


