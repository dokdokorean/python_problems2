a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
if a[1]>b[0]:
                print('cross')
else:
                print('not cross')
