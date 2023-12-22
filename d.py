f = ["a", "a", "b", "a"]
o = ["a", "b", "a"]
co = o.copy()
d = 0
for i in range(len(co)):
    g = 0
    while co[i] == f[d]:
        g += 1
        if d < len(f)-1:
            d = d + 1
    o[i] = co[i] * g
print(o)
