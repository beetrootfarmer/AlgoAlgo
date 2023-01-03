import sys
input=sys.stdin.readline

N = int(input().strip())
sangguen = list(map(int, input().strip().split()))
sangguen_dict = {}
for s in sangguen:
    if s not in sangguen_dict:
        sangguen_dict[s] = 1
    else:
        sangguen_dict[s] += 1

M = int(input().strip())
data = list(map(int, input().strip().split()))
for d in data:
    if d in sangguen_dict:
        print(sangguen_dict[d], end=' ')
    else:
        print(0, end=' ')
print()