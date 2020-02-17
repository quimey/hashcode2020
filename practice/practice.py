import sys

m, n = map(int, input().split())
s = list(map(int, input().split()))
s = [(p, i) for i, p in enumerate(s)]

res = {0: 0}
s.sort(reverse=True)

best = 0

for p, i in s:
    print(i, best, len(res), file=sys.stderr)
    for r in res.copy():
        if r + p <= m and r + p not in res:
            best = max(best, r + p)
            res[r + p] = (i, p)

a = max(res.keys())
u = []
while a:
    i, p = res[a]
    u.append(str(i))
    a -= p
print(len(u))
print(' '.join(u))
