f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

directions = {
  "UPPER-LEFT": (-1, -1),
  "UPPER": (-1, 0),
  "UPPER-RIGHT": (-1, 1),
  "LEFT": (0, -1),
  "RIGHT": (0, 1),
  "LOWER-LEFT": (1, -1),
  "LOWER": (1, 0),
  "LOWER-RIGHT": (1, 1),
}

def count_splits(pos: tuple[int, int], already_visited: set[tuple[int, int]]) -> int:
  if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
    return 0
  if pos in already_visited:
    return 0
  already_visited.add(pos)
  if lines[pos[0]][pos[1]] == "^":
    return 1 \
      + count_splits((pos[0] + directions["LEFT"][0], pos[1] + directions["LEFT"][1]), already_visited) \
      + count_splits((pos[0] + directions["RIGHT"][0], pos[1] + directions["RIGHT"][1]), already_visited)
  return count_splits((pos[0] + directions["LOWER"][0], pos[1] + directions["LOWER"][1]), already_visited)

S_pos = (0, lines[0].index("S"))
res = count_splits(S_pos, set())
print(res)