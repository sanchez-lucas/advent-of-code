f = open("input.txt", "r")
rows = [list(l.strip()) for l in f.readlines()]

matrix = {
  "UPPER-LEFT": (-1, -1),
  "UPPER": (-1, 0),
  "UPPER-RIGHT": (-1, 1),
  "LEFT": (0, -1),
  "RIGHT": (0, 1),
  "LOWER-LEFT": (1, -1),
  "LOWER": (1, 0),
  "LOWER-RIGHT": (1, 1),
}

def adjacent_items_count(rows, i, j):
  count = 0
  for direction in matrix.values():
    di, dj = direction
    ni, nj = i + di, j + dj
    if 0 <= ni < len(rows) and 0 <= nj < len(rows[0]):
      if rows[ni][nj] == '@':
        count += 1
  return count

res = 0
sub_res = 0
while True:
  tiles_to_replace = []
  for (i, row) in enumerate(rows):
    for (j, item) in enumerate(row):
      if item == '@':
        adj_count = adjacent_items_count(rows, i, j)
        if adj_count < 4:
          sub_res += 1
          tiles_to_replace.append((i, j))
  res += sub_res
  if sub_res == 0:
    break
  for (i, j) in tiles_to_replace:
    rows[i][j] = '.'
  tiles_to_replace = []
  sub_res = 0

print(res)