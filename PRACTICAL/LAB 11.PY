# Map Coloring using CSP

# Map of neighboring regions
map = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store the assigned colors
assignment = {}


def is_safe(region, color):
    for neighbor in map[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve():
    # If all regions are colored
    if len(assignment) == len(map):
        return True

    # Select an uncolored region
    region = next(r for r in map if r not in assignment)

    # Try each color
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if solve():
                return True

            # Backtrack
            del assignment[region]

    return False


# Solve the CSP
if solve():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("No solution exists")
