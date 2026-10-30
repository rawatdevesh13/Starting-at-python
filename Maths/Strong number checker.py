n=int(input('Enter the number: '))
a=n
b=0
x=0
z=0
y=0
if n==0:
    x=1
else:
    while n>0:
        x=x+1
        n=n//10
for i in range (1,x+1,1):
    y=(a%(10**i))//(10**(i-1))
    f=1
    for j in range (1,y+1,1):
        f=f*j
    z=z+f
if z==a:
    print('It is a strong number')
else:
    print('It is not a strong number')
