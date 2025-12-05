f = open("input.txt", "r")
ranges, ids = [section.split("\n") for section in f.read().split("\n\n")]
ranges = [tuple(map(int, r.split("-"))) for r in ranges]

def ranges_overlap(r1, r2):
  return r1[0] <= r2[1] and r2[0] <= r1[1]

merged_ranges = []

merge = True
while merge:
  merge = False
  for i in range(len(ranges)):
    r1 = ranges[i]
    for j in range(i + 1, len(ranges)):
      r2 = ranges[j]
      if ranges_overlap(r1, r2):
        new_range = (min(r1[0], r2[0]), max(r1[1], r2[1]))
        ranges.pop(j)
        ranges.pop(i)
        ranges.append(new_range)
        merge = True
        break
    if merge:
      break

print(sum(r[1] - r[0] + 1 for r in ranges))