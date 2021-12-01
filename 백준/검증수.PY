L = map(int,input().split())
s = 0
for i in L:
    s += (i**2)
print(s%10)