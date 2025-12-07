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

def count_timelines(pos: tuple[int, int], pos_timelines_cache: dict) -> int:
  if pos in pos_timelines_cache:
    return pos_timelines_cache[pos]
  if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
    pos_timelines_cache[pos] = 1
    return 1
  if lines[pos[0]][pos[1]] == "^":
    left_timelines = count_timelines((pos[0] + directions["LEFT"][0], pos[1] + directions["LEFT"][1]), pos_timelines_cache)
    right_timelines = count_timelines((pos[0] + directions["RIGHT"][0], pos[1] + directions["RIGHT"][1]), pos_timelines_cache)
    timelines = left_timelines + right_timelines
    pos_timelines_cache[pos] = timelines
    return timelines
  timelines = count_timelines((pos[0] + directions["LOWER"][0], pos[1] + directions["LOWER"][1]), pos_timelines_cache)
  pos_timelines_cache[pos] = timelines
  return timelines

S_pos = (0, lines[0].index("S"))
res = count_timelines(S_pos, {})
print(res)