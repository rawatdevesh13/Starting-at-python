n=int(input('Enter a positive integer: '))
y=0
x=1
print('The factors of',n,'are as follows:')
for i in range (1,n+1,1):
    y=n%x
    if y==0:
        print(x,"               ",n//x)
    x=x+1
    if x>n**(1/2):
        break
