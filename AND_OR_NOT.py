my_fev_no = 1
my_least_fev_no =5
a_neutral_no = 3

#AND CONDITION
print(my_fev_no)
print(my_least_fev_no > 0)

print(my_fev_no > 0 and my_fev_no<=3)
print(my_fev_no<0 and my_fev_no<=3)
print(my_fev_no >0 and my_fev_no >=3)

#OR CONDITION
a_neutral_no = 3
print(a_neutral_no == 3 or my_fev_no <0)
print(a_neutral_no !=3 or my_fev_no <0)
print(my_fev_no < 0 or True)

#NOT operato its reverse the result
print(a_neutral_no)

print(not a_neutral_no ==3)
print(not a_neutral_no < 0)