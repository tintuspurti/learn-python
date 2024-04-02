a_variable= 23
is_today_saturday=False
my_fevorite_car="mustang"
the_3_heros=["ranveer","ajay","govinda"]

print(a_variable)
print(type(a_variable))
print(type(is_today_saturday))
print(type(my_fevorite_car))
print(type(the_3_heros))
#int                          
large_no=234242223203830984609
#float
pi=3.14343433
scifi= 1e-2
print(large_no)                          
print(type(large_no))
print(type(pi))
print(type(scifi))
print(float(a_variable))
print(int(pi))
print(type(10/5))
print(type(10//5))
print(type(is_today_saturday))
#boolean
cost_of_icebag =1.5
is_icebag_expensive =cost_of_icebag >=10
print(is_icebag_expensive)
print(type(is_icebag_expensive))
print(type(bool(1.2)))
#nothing
nothing =None
print(type(nothing))
#string
today= "saturday"
time= "12:0"
print(today + " " + time)
print(today[3])
print(today[5:8])
#.lower,.upper.,.capitilize
print(today.upper())
print(today.capitalize())
#fomat intresting to me
cost_of_icebag = 1.25
profit_margin =.3
number_of_bags = 500
output_template = """is a grocery store sells ice bags at ${}
per bag, with a profit margin of {} %, then the total profit
it total profit it makes by selling {} ice bags is $ {}. """
print(output_template)
total_profit = cost_of_icebag*profit_margin*number_of_bags
output_msg = output_template.format(cost_of_icebag, profit_margin*500,number_of_bags, total_profit)
print(output_msg)