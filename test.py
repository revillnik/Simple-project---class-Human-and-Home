z = [i for i in (input().split(" "))]
z.insert(0, z[0])
f = z.copy()
for i in range(len(z) - 1):
    while z[i] == z[i + 1]:
        z[i] = ""
        k = "".join(z)
o = list(k)
g = 0
v = []
for i in range(len(o)):
    for d in range(len(f)):
        while o[i] == f[d]:
            g += 1
    o[i] = o[i] * g
    h = list(o[i])
    v.append(h)
v[0].pop(0)
print(v)
