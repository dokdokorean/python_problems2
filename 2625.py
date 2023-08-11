n=int(input())
count=0
l=[]
for i in range(1,n//2+1):
         for j in range(1,n//2+1):
                         k=n-i-j
                         a=sorted([i,j,k])
                         if a[0]+a[1]>a[2] and a not in l:
                                         l.append(a)
                                         count+=1
print(count)
         
         
