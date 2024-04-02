fruits =['apple', 'banana','cherry']
print(type(fruits))
a_list = [23, 'hello', None, 3.14, fruits, 3<=5,True]
print(type(23))
print(type(None))
print(a_list)

empty_list =[]
print(type(empty_list))
#len
print(len(fruits))
#index
print(fruits[2])
print(fruits[-2])
print(a_list[2:5])
#change the value
fruits[2] = 'blueberry'
print(fruits)
#add velue
fruits.append('dates')
print(fruits)
#add new values b/w specific index
fruits.insert(2,'graps')
print(fruits)
#remove
fruits.remove('blueberry')
print(fruits)
#remove elment
fruits.pop(1)
print(fruits)
#to check values existence
print('cherry' in fruits)
#join the operator
more_fruits = fruits + ['pineapple','tomato']+['dates','banana']
print(more_fruits)
#copy 
more_fruits_copy=more_fruits.copy()
print(more_fruits_copy)
#modify and original remain unchanged
more_fruits_copy.remove('pineapple')
print(more_fruits_copy)