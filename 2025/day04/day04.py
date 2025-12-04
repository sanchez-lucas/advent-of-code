f = open("input.txt", "r")
rows = [l.strip() for l in f.readlines()]

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
for (i, row) in enumerate(rows):
  for (j, item) in enumerate(row):
    if item == '@':
      res += 1 if adjacent_items_count(rows, i, j) < 4 else 0

print(res)