f = open("input.txt", "r")
blocks = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

distances = {}

max_area = 0
for y, x in blocks:
  for yy, xx in blocks:
    if (y, x) == (yy, xx):
      continue
    dist_y = abs(y - yy)
    dist_x = abs(x - xx)
    area = (dist_y + 1) * (dist_x + 1)
    if area > max_area:
      max_area = area

print(max_area)
