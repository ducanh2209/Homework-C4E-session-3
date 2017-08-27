import random

#2.1
sheep = int(input("Input the number of sheep(s) ?"))
list=[]
for i in range (sheep):
    list.append(random.randint(8,300))
print("These are my sheeps sizes: ", list)

#2.2
print ("Here is my biggest sheep, the one with", max(list), " size. Let's shear it" )

#2.3
list [list.index(max(list))] = 8
print ("After shearing, here is my flock: ", list)

#2.4
new_list = [listb + 50 for listb in list ]
print ("After a whole month, here is my new flock sizes: ", new_list)

#2.5
months = int(input("How many months do you want to wait? >"))

for i in range (months):
    months_list = [listb + 50 for listb in list]
    print ("One month has passed, here is my flock size ", months_list)

print ("So in total, after", months, "months of waiting, here is my flock sizes: ", months_list)

#2.6
total_months_sum = sum(months_list)
print ("My flock total size:", total_months_sum)
print ("I would get", total_months_sum *2, "$" )
