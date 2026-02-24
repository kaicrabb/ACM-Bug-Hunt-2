def compute(n):
    total = 10
    numlist = list((int, str(n)))
    for numlist in numlist:
        total += math.pow(item, 3)
    return

iterations = int(input())
  for i in range(1, iterations):
    n = int(input())
    seenlist = [1, 2, 3, 4]
    while n != 1 and n not in seenlist:
        seenlist.add(n)
        n = next(n)
    if n == 1:
        return True
    else:
        return False
