a=list(map(int,input().split()))
hap=0
for i in a:
    if i%2==1:
        hap+=i
if hap==0:
    print("-1")
else:
    print(hap)

    
