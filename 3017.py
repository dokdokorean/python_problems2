n=int(input())
l=list()
for i in range(n):
    a,b=map(int,input().split())
    l.append([i+1,a,b])
l.sort(key=lambda x:(x[1],x[2]),reverse=True)
for i in l:
    for j in i:
        print(j, end=' ')
    print()
