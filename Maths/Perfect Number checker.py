n=int(input('Enter the number: '))
a=n
b=0
x=0
z=0
for i in range (1,n,1):
    b=n%i
    if b==0:
        z=z+i
    else:
        z=z+0
if z==a:
    print('It is a perfect number')
else:
    print('It is not a perfect number')
