n=int(input('Enter the number'))
a=n//2
b=2
z=0
x=0
y=0
z=0
for i in range (1,a+1,1):
    x=n%b
    b=b+1
    if x==0:
        print('Composite Number')
        break
else:
    print('Prime Number')