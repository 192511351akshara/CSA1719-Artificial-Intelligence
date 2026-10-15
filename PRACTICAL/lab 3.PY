
from collections import deque

jug1, jug2 = 4, 3
target = 2

queue = deque([(0, 0)])
visited = set()

while queue:
    a, b = queue.popleft()

    if (a, b) in visited:
        continue
    visited.add((a, b))

    print(a, b)

    if a == target or b == target:
        print("Target reached!")
        break

    states = [
        (jug1, b),
        (a, jug2),
        (0, b),
        (a, 0),
        (a - min(a, jug2 - b), b + min(a, jug2 - b)),
        (a + min(b, jug1 - a), b - min(b, jug1 - a))
    ]

    for state in states:
        if state not in visited:
            queue.append(state)
