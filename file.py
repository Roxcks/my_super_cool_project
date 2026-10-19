pos = input()
col = ord(pos[0]) - ord('a')
row = 8 - int(pos[1])

matrix = [['.'] * 8 for _ in range(8)]

matrix[row][col] = 'N'

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1)
]

for m in moves:
    new_row = row + m[0] 
    new_col = col + m[1]  
    
    if 0 <= new_row < 8 and 0 <= new_col < 8:
        matrix[new_row][new_col] = '*'

for row_elements in matrix:
    print(*row_elements)
