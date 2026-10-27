n=int(input('Enter the number: '))
a=0
b=0
c=n
x=0
y=0
z=c
d=n
while c>0:
    if c<10:
        print('The digital root of', d, 'is', c)
        break
    while c>0:
        x=x+1
        c=c//10
    for i in range (1,x+1,1):
            b=(z%(10**i))//(10**(i-1))
            y=y+b
    c=y
    z=c
    x=0
    a=0
    y=0
if c==0:
    print('The digital root of 0 is 0')