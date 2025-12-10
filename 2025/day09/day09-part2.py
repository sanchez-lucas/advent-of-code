f = open("input.txt", "r")
blocks = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
limits = set()
for i in range(len(blocks) - 1):
  block_1 = blocks[i]
  block_2 = blocks[i + 1]
  for x in range(min(block_1[0], block_2[0]), max(block_1[0], block_2[0]) + 1):
    for y in range(min(block_1[1], block_2[1]), max(block_1[1], block_2[1]) + 1):
      limits.add((x, y))
block_1 = blocks[-1]
block_2 = blocks[0]
for x in range(min(block_1[0], block_2[0]), max(block_1[0], block_2[0]) + 1):
  for y in range(min(block_1[1], block_2[1]), max(block_1[1], block_2[1]) + 1):
    limits.add((x, y))

blocks = set(blocks)

def is_inside(x: int, y: int) -> bool:
  if (x, y) in limits:
    return True
  edges = 0
  last_encounter_was_limit = False
  max_x = max(xx for xx, yy in blocks)
  for xx in range(x + 1, max_x + 2):
    if (xx, y) in limits and not last_encounter_was_limit:
      edges += 1
      last_encounter_was_limit = True
    elif (xx, y) not in limits:
      last_encounter_was_limit = False
  return edges % 2 == 1

# area = set(limits)
# min_x = min(x for x, y in blocks)
# max_x = max(x for x, y in blocks)
# min_y = min(y for x, y in blocks)
# max_y = max(y for x, y in blocks)
# for x in range(min_x, max_x + 1):
#   for y in range(min_y, max_y + 1):
#     if is_inside(x, y):
#       area.add((x, y))

max_area = 0
for i, (x, y) in enumerate(blocks):
  for j, (xx, yy) in enumerate(blocks):
    if (x, y) == (xx, yy):
      continue
    inverse_1 = (x, yy)
    inverse_2 = (xx, y)
    dist_y = abs(y - yy)
    dist_x = abs(x - xx)
    area = (dist_y + 1) * (dist_x + 1)
    another_block_in_area = False
    if area <= max_area:
      continue
    for xxx, yyy in limits:
      if (xxx, yyy) == (x, y) or (xxx, yyy) == (xx, yy):
        continue
      if min(x, xx) < xxx < max(x, xx) and min(y, yy) < yyy < max(y, yy):
        another_block_in_area = True
        break
    if not another_block_in_area \
    and is_inside(inverse_1[0], inverse_1[1]) and is_inside(inverse_2[0], inverse_2[1]):
      max_area = area
print(max_area)
#     in_area = True
#     for i in range(min(x, xx), max(x, xx) + 1):
#       for j in range(min(y, yy), max(y, yy) + 1):
#         if (i, j) not in area:
#           in_area = False
#           break
#       if not in_area:
#         break
#     if in_area:
#       dist_y = abs(y - yy)
#       dist_x = abs(x - xx)
#       area_size = (dist_y + 1) * (dist_x + 1)
#       if area_size > max_area:
#         max_area = area_size

# print(max_area)

# max_area = 0
# for x, y in blocks:
#   for xx, yy in blocks:
#     if (x, y) == (xx, yy):
#       continue
#     dist_y = abs(y - yy)
#     dist_x = abs(x - xx)
#     area = (dist_y + 1) * (dist_x + 1)
#     inverse_1 = (y, x)
#     inverse_2 = (yy, xx)
#     l_blocks = list(blocks)
#     if inverse_1 in limits and inverse_2 in limits and area > max_area:
#       max_area = area

# print(max_area)