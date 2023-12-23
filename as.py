n, m = int(input()), int(input())
z = []
f = ''
s = ''
for i in range (n):
    for r in range (m):
        f = s
        s = input()
        f = f + ' ' + s
        print(f)
    z.append(f.split())
print(z)