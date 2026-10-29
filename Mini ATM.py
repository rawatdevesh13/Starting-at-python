x=1000
n=1
print('''===== MINI ATM =====
1.Enter bank
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Exit''')
while n !=5:
    n=int(input('Enter your choice: '))
    if n==1:
        print('Welcome to the bank1')
    elif n==2:
        print('Your balance is',x)
    elif n==3:
        y=int(input('Enter deposit amount: '))
        if y>0:
            x=x+y
            print('Your balance is:',x)
        elif y==0 :
            print('No amount deposited')
        else:
            print('''Error only positive amounts can be deposited
For negative deposition (Which means withdrawl) use choice 4''')
    elif n==4:
        z=int(input('Enter withdraw amount: '))
        if z<0:
            print('''Error only positive amounts can be withdrawn
For negative withdrawls (Which means Deposition) use choice 3)''')
        elif z>0 and z<x:
            x=x-z
            print('Your balance is:',x)
        elif z==0:
            print('No amount withdrawn!')
        elif z==x:
            x=x-z
            print('Your balance is 0!')
        else:
            print('Amounts greater than your ATM wallet cannot be taken!')
            print('Your balance is' ,x,)
            print('Please reenter the withdrawl amount correctly!')
    elif n==5:
        break
    else:
        print('''Error
Such a choice does not exist''')
