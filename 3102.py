l=list()
def push(x):
    l.append(x)
def top():
    if l:
        print(l[-1])
    else:
        print(-1)
def pop():
    if l:
        l.pop()
def size():
    print(len(l))
def empty():
    if l:
        print('false')
    else:
        print('true')
n=int(input())
for i in range(n):
    a=input()
    eval(a)
    
