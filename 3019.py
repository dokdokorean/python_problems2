n=int(input())
l=list()
for i in range(n):
    a,b,c,d=input().split()
    b=int(b)
    c=int(c)
    d=int(d)
    l.append([a,b,c,d])
l.sort(key=lambda x:(x[1],x[2],x[3],x[0]))
for i in l:
    print(i[0])
    
