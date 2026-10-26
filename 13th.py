n=int(input('Enter the number'))
x=0
for i in range (0,n+1,1):
    if (x*x)==n:
        print('Perfect square of',x)
        break
    x=x+1
else:
    print ('Not a perfect square')