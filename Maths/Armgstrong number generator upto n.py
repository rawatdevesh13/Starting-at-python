n=int(input('Enter the number: '))
a=0
x=0
b=0
y=0
z=0
c=0
print('Armstrong numbers upto',n,'are:')
for i in range (0,n+1,1):
    a=y
    while y>0:
        x=x+1
        y=y//10
    for i in range (1,x+1,1):
        c=(a%(10**i))//(10**(i-1))
        b=b+c**x
    if b==a:
        print(b)
    else:
        pass
    z=z+1
    y=z
    x=0
    b=0