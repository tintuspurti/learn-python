person1 ={
    'name': 'john doe',
    'sex': 'male',
    'age': 32,
    'married': True
}   
print(person1)
print(type(person1))

#create a dictionary usin dict func
person2 = dict(name='jane judy', sex ='female', age =28, married = False)
print(person2)
print(type(person2))

# '[]'acess the value
print(person1['name'])
#'Get' is also for acess the value
print(person2.get('age'))
print(person1.get('name','sex'))
#"in" to check a key present in dictionary
print('name' in person2)
print('sex' in person2)
# []= to change the values
person1['married']=False
print(person1['married'])
#to add values 
person2['adress'] ='1, penny lane'
print(person2)
#to remove values
person2.pop('adress')
print(person2)
#to view the list of keys, values, keyvalues pairs
print(person1.keys())
print(person1.values())
print(person2.items())
print(person1.items())


#what happen if you use the same key multiple times while creating a dictionary
person3= (person1, person2)
person_x=person_y =person3
print(person_x)
print(person_y)

#how can you create a copy dictionary
dublicate_person_dictionary=person1.copy()
print(dublicate_person_dictionary)

#can the value associated with key itself be dictionary
#cant understan this question

#how can you you add the key values pair from one dictionary into another dictionary
person1['contact'] ='983928','mobile no'
print(person1.keys(),person1['contact'])

#can the keys of dictionary be something other than a string e.g :number, boolean, list
person5={
    1: 'sameer',
    True: 'anand',
 #  'listA','listB','listc': 'listkey'  "this line shown error so list key cant be dictionary"
}
print(person5)




