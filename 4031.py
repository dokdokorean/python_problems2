a=list(map(int,input().split()))
b=[0]
c=[0]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(max(b)+max(c))
