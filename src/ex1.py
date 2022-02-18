tests = [
  ['ABCDCDC', 'CDC'], # out -> 2
  ['ABCDCDC', 'CD'],  # out -> 2
  ['ABCDCDC', 'C'],   # out -> 3
  ['LLLLLLL', 'L'],   # out -> 7
  ['LLLLLLL', 'LL'],  # out -> 6
]


def count_sub(s1, s2):
  count = 0

  for idx in range(len(s1)):
    if s2 == s1[ idx: idx+len(s2) ]:
      count = count +1
  return count


for test in tests:
  print(count_sub(test[0],test[1]))