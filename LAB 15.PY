# Decision Tree using ID3 Algorithm

from math import log2

data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rainy', 'Cool', 'Yes'],
    ['Rainy', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Overcast', 'Cool', 'Yes']
]

def entropy(rows):
    total = len(rows)
    counts = {}

    for row in rows:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    result = 0
    for count in counts.values():
        p = count / total
        result -= p * log2(p)

    return result

def information_gain(rows, column):
    total_entropy = entropy(rows)
    values = set(row[column] for row in rows)

    weighted_entropy = 0

    for value in values:
        subset = [row for row in rows if row[column] == value]
        weighted_entropy += (len(subset) / len(rows)) * entropy(subset)

    return total_entropy - weighted_entropy

# Find best attribute
best_column = max(range(2), key=lambda c: information_gain(data, c))

print("Decision Tree")
print("Best Attribute:", ["Weather", "Temperature"][best_column])

for value in set(row[best_column] for row in data):
    subset = [row for row in data if row[best_column] == value]
    labels = [row[-1] for row in subset]

    print(value, "->", max(set(labels), key=labels.count))
