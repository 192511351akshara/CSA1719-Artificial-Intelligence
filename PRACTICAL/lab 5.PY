
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

queue = deque([(start, [])])
visited = {start}

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        for step in path + [state]:
            print(step)
        break

    for x, y in moves:
        if boat == 1:
            nm, nc, nb = m - x, c - y, 0
        else:
            nm, nc, nb = m + x, c + y, 1

        mr, cr = 3 - nm, 3 - nc

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            if (nm == 0 or nm >= nc) and (mr == 0 or mr >= cr):
                new_state = (nm, nc, nb)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))
    # Continue searching until the goal is found
else:
    print("No solution found")
