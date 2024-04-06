result=1
i=1
while i<=100:
    result=result*i
    i=i+1
print('the factorial of 100{}'.format(result))

#factorial fo 1000
 
result =1
o=1
while o<= 1000:
    result *= o
    o+=1
print('factorial of thousand ',result)

# making diagram with star
line ='*'
max_length = 10
while len(line) <= max_length:
    print(line)
    line +="*"
while len(line) > 0:
    print(line)
    line = line[:-1] 
