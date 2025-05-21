left = []
right = []
distances = {}

with open('input.txt') as f:
    for line in f:
        l, r = line.rstrip('\n').split('   ')
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
result = 0

for i in range(len(left)):
    l = left[i]
    r = right[i]

    distance = abs(l-r)
    result += distance

print(result)