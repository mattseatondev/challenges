
def is_adjacent(mat, node_one, node_two):
    return True if mat[node_one][node_two] else False


matrix = [
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]

print(is_adjacent(matrix, 0, 1))
print(is_adjacent(matrix, 3, 4))