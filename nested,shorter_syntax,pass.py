a_number = 15
if a_number % 2 ==0:
    print('{} is even'.format(a_number))
    if a_number % 3==0:
        print('{} is also divisible by 3'.format(a_number))
    else:
        print('{}is not divisible by 3'.format(a_number))
else:
    print("{} is odd ".format(a_number))
    if a_number % 5==0:
        print('{}is also devisible by 5'.format(a_number))
    else:
        print('{} is not divisible by 5'.format(a_number))

#if conditional expression
a_number=13
if a_number %2==0:
    parity= 'even'
else:
    parity="odd"
print('the number{}is{}'.format(a_number,parity))

#shorter syntax
parity = 'even' if a_number%2==0 else 'odd'
print('the number{}is{}'.format(a_number,parity))



#the pass statement
''' #this contain syntax error!
a_number = 9
if a_number%2==0:
    elif a_number % 3==0:
    print('{}is divisible by 3   but not by 2'.format(a_number))'''

a_number=9
if a_number%2==0:
    pass
elif a_number%3==0:
    print('{} is divisble by 3 but not with 2'.format(a_number) )

