z = [i for i in (input().split(" "))]
f = z.copy()
for i in range(len(z) - 1):
    while z[i] == z[i + 1]:
        z[i] = ""
        k = "".join(z)
o = list(k)
co = o.copy()
d = 0
print(f)
print(o)
for i in range(len(co)):
	g = 0 
	while co[i] == f[d]:
		g += 1
		d += 1
	o[i] = o[i] * g
print(o)
