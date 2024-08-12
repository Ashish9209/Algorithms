arr = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]
binary_indexed_tree = [1, 8, -13, 4, 7, -6, 12, 14, 2, -8, 16, 3]

i = 1

nxt = i + (i & -1)
binary_indexed_tree[nxt - 1] += binary_indexed_tree[i - 1]

for i in range(2, len(binary_indexed_tree)):
  nxt = i + (i & -i)
  if nxt - 1 >= len(binary_indexed_tree):
    continue
  binary_indexed_tree[nxt - 1] += binary_indexed_tree[i - 1]

print(binary_indexed_tree)