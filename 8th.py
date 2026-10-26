n=int(input('Enter the number: '))
x=0
while n>0:
    n=n//10
    x=x+1
print('The number of digits are',x)
