n=int(input('Enter the number: '))
a=n
x=0
b=0
while n>0:
    x=x+1
    n=n//10
for i in range (1,x+1,1):
    y=(a%(10**i))//(10**(i-1))
    b=10*b+y
if b==a:
    print("It is a palindrome")
else:
    print('It is not a palindrome')
