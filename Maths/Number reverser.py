n=int(input('Enter the number: '))
a=n
b=0
x=0
y=0
while n>0:
    x=x+1
    n=n//10
for i in range (1,x+1,1):
    b=(a%(10**i))//(10**(i-1))
    y=y*10+b
print(y)
