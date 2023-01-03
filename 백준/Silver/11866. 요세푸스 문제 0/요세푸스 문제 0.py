N, K = map(int, input().split())

q = [i for i in range(1, N+1)]
result = []

while q:
    for _ in range(K-1):
        t = q.pop(0)
        q.append(t)
    d = q.pop(0)
    result.append(d)

print('<'+', '.join(map(str, result))+'>')