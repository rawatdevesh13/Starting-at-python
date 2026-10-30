n=int(input('Enter the number till which the prime exponent for the perfect number is going to be used!: '))
a=0
b=1
z=0
y=[]
x=0
m=0
t=0

for i in range(2,n+1,1):
    z=0
    for j in range(2,i,1):
        if i%j==0:
            z=1
            break
    if z==0:
        y.append(i)

for k in range(0,len(y),1):
    x=y[k]
    m=(2**x)-1
    if x==2:
        print(6)
    else:
        s=4
        for j in range(0,x-2,1):
            s=((s*s)-2)%m
        if s==0:
            print((2**(x-1))*m)
