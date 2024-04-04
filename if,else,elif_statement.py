#if statement
a_number=34

if a_number % 2 ==0 :
    print("we're inside an if block")
    print('the given number {} is even'.format(a_number))

#another example
another_number = 33
if  another_number % 2 ==0 :
    print("we're inside an if block")
    print('the given number {} is even'.format(a_number))

#else statement
b_number =36
if b_number % 2 == 0:
    print('the given number {} is even'.format(b_number))
else:
    print('the given numebr {} is odd' .format(b_number))

#another example
c_number =37
if c_number % 2 == 0:
    print('the given number {} is even'.format(c_number))
else:
    print('the given numebr {} is odd' .format(c_number))

#string example
three_herose =('ram','ajay','rahul')
a_hero="salman"
if a_hero in three_herose :
    print('{} is the herose'.format(a_hero))
else:
    print('{} is not herose'.format(a_hero))


#elif statement
today= 'wednesday'

if today =='monday':
    print("today is day of moon")
elif today=='tuesday':
    print("today is the day of tyr")
elif today =='wednesday':
    print('today is the day of odin')
elif today=='thursday':
    print("today is the day of thor")
elif today=='friday':
    print("today is tha day of fry")
elif today=='saturday':
    print("today is the day of sat")

#another example 

c_number = 15
if c_number % 2 ==0:
    print('{} is deivisible by 3.'.format(c_number))
elif c_number % 3==0:
    print('{} is divisible by 3'.format(c_number))
elif c_number % 5==0:
    print('{} is divisible by 5'.format(c_number))
elif c_number % 7==0:
    print('{} is divisible by 7 '.format(c_number))

#combine all if, else and elif

d_number=49

if d_number % 2 ==0:
    print('{} is divisible by 2'.format(d_number))
elif d_number% 3 == 0:
    print('{} is divisible by 3'.format(d_number))
elif d_number %5 ==0:
    print('{} is divisible by 5 '.format(d_number))
else:
    print(' all check is failed')
    print('{} is not divisible by 2,3,5'.format(d_number))


#using AND condition
e_number= 12
if e_number % 3==0 and e_number % 5==0:
    print('the values{} is divisible by 3 and 5'.format(e_number))
elif not e_number  % 5 ==0:
    print('the number {} is not divisible by 5 '.format(e_number))

#non boolean condition
if '':
    print('the conditions evaluated to true')
else:
    print('the conditions evaulauted to false')

if {'a':34}:  #dictionary
    print('the conditions evaluated to true')
else:
    print('the conditions evaulauted to false')

