items = ["T-Shirt", "Sweater", ]
loop_continue = True

print ("Hello customer, what's your name", end = '')
name = input ("?  ")
print("what's your preference for clothes ?")
print ("1 for male clothes")
print ("2 for female clothes")
print ("3 for both")
gender = int(input ("Preference number " ))

def crud():
    print ("C stands for Create" )
    print ("R stands for Read")
    print ("U stands for Update")
    print ("D stands for Delete ")

if gender == 1:
    print ("Welcome to our shop. Our clothes suit a classy man, what do you want to do, MR " + name + "? (C, R, U, D) ")
    crud()
elif gender == 2:
    print ("Welcome to our shop. Our clothes suit a beautiful woman, what do you want to do, MRS/MISS "+ name + "? (C, R, U, D)")
    crud()
elif gender == 3:
    print ("Welcome to our shop. Our clothes suit a fabulous person, what do you want to do? (C, R, U, D)")
    crud()
else:
    print ("Please follow the order")


while True:
    choice= str(input("I choose to "))
    if [choice == "C"] or [choice == "c"] :
            print (items)
            new_item = input("Enter new item")
            items.append(new_item)
            print("New list will be", items)

    elif [choice == "R"] or [choice == "r"]:
            print (items)
            item_no = 1

    elif [choice == "U"] or [choice == "u"]:

            position = int(input("Update position? "))
            new_item_name = input("New item? ")
            items[position - 1] = new_item_name
            print("New list will be" + items)

    elif [choice == "D"] or [choice == "d"]:
            print (items)
            position = int(input("Delete position? "))
            items.pop(position - 1)
            print("New list will be" + items)


    else:
            print ("Wrong input")
            crud ()

