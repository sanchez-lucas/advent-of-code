f = open("input.txt", "r")
points = [tuple(map(int,line.strip().split(','))) for line in f.readlines()] # 3D points as [(x, y, z)]

distances = {}
for x, y, z in points:
  for xx, yy, zz in points:
    if (x, y, z) == (xx, yy, zz):
      continue
    dist = (x - xx) ** 2 + (y - yy) ** 2 + (z - zz) ** 2
    points_tuple = (x, y, z, xx, yy, zz)
    inverse_points_tuple = (xx, yy, zz, x, y, z)
    if inverse_points_tuple not in distances:
      distances[points_tuple] = dist

circuits = [set([point]) for point in points]
for (x, y, z, xx, yy, zz), _distance in sorted(distances.items(), key=lambda item: item[1])[:1000]:
  pair_already_connected = False
  for circuit in circuits:
    if (x, y, z) in circuit and (xx, yy, zz) in circuit:
      pair_already_connected = True
      break
  if pair_already_connected:
    continue
  first_found_circuit = None
  second_found_circuit = None
  for circuit in circuits:
    if (x, y, z) in circuit:
      first_found_circuit = circuit
      break
  for circuit in circuits:
    if (xx, yy, zz) in circuit:
      second_found_circuit = circuit
      break
  for point in second_found_circuit:
    first_found_circuit.add(point)
  circuits.remove(second_found_circuit)

res = 1
for circuit in sorted(circuits, key=lambda c: len(c), reverse=True)[:3]:
  res *= len(circuit)
print(res)