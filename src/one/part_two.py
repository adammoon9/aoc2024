similarities = {} # frequency dict

left = []
distances = {}

with open('input.txt') as f:
    for line in f:
        l, r = line.rstrip('\n').split('   ')
        left.append(int(l))
        similarities[int(r)] = similarities.get(int(r), 0) + 1
        
result = 0

for n in left:
    result += n * similarities.get(n, 0)

print(result)   