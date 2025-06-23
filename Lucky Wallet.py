# اول طريقة
import random
print("Welcome to 'whose wallet!' ")
print("You will give me a list of names, and I will pick a person to pay")
names_string = input("If you're ready, enter the names separated by a comma ")
names = names_string.split(", ")
length = len(names) -1
random_number = random.randint(0,length)
random_person = names[random_number]
print(f"Please ask '{random_person}' to take his wallet out. Dinner is on him")


# تاني طريقة
import random
print("Welcome to 'whose wallet!' ")
print("You will give me a list of names, and I will pick a person to pay")
names = input("If you're ready, enter the names separated by a comma ").split(", ")
print(f"Please ask {random.choice(names) } to take his wallet out. Dinner is on him.")

# تالت طريقة
import random
print("Welcome to 'whose wallet!'\nYou will give me a list of names, and I will pick a person to pay ")
print(f"Please ask {random.choice(input("enter the names separated by a comma: ") .split(", ")) } to take his wallet out. Dinner is on him.")