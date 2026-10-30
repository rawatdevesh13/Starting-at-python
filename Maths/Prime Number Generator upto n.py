n= int(input("Enter the limit: "))
x=0
y=3
z=1
a=2
print("The prime numbers upto",n,"are:")
print(2)
for i in range (1,n,1):
    b=y//2
    for j in range (1,b+1,1):
        x=y%a
        a=a+1
        if x==0:
            break
    else:
        print(y)
    y=y+1
    a=2