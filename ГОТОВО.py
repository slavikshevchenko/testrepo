# С.52
names = ['Kaban', 'Fenia']
print(names[0])
print(names[-1])

SMS1 = f"Who are you {names[0]}"
SMS2 = f"Who are you {names[1]}"
print(SMS1)
print(SMS2)

mooto = ['BMW', 'Harley-Davidson', 'Honda', 'Husgvarna', 'Kawasaki']
like = f"I would like to buy a motorcycle {mooto[1]}"
print(like)

# C.58
guests1 = ['Horse', 'Elephant', 'Turtle']
guest1 = guests1[0]
guest2 = guests1[1]
guest3 = guests1[2]
print(f"Hi {guest1}, I invite you on 19.06 for Dr.")
print(f"Hi {guest2}, I invite you on 19.06 for Dr.")
print(f"Hi {guest3}, I invite you on 19.06 for Dr.")

guests1[1] = 'Mouse'
guest1 = guests1[0]
guest2 = guests1[1]
guest3 = guests1[2]
print(f"Hi {guest1}, I invite you on 19.06 for Dr.")
print(f"Hi {guest2}, I invite you on 19.06 for Dr.")
print(f"Hi {guest3}, I invite you on 19.06 for Dr.")

guests1.insert(0, 'Dog')
guests1.insert(1, 'Duck')
guests1.append('Spider')
print(guests1)

error1 = guests1.pop()
print(f"Sorry {error1}, there aren't enough seats.")
error2 = guests1.pop()
print(f"Sorry {error2}, there aren't enough seats.")
error3 = guests1.pop()
print(f"Sorry {error3}, there aren't enough seats.")
error4 = guests1.pop()
print(f"Sorry {error4}, there aren't enough seats.")
print(guests1)

guest1 = guests1[0]
guest2 = guests1[1]
print(f"{guest1} the invitation still stands")
print(f"{guest2} The invitation still stands")

del guests1[0]
del guests1[0]
print(guests1)

# C.61
Country = ['Australia', 'Indonesia', 'Netherlands', 'Iceland', 'Greece']
print(Country)
print(sorted(Country))
print(Country)
print(sorted(Country, reverse=True))
print(Country)
Country.reverse()
print(Country)
Country.reverse()
print(Country)
Country.sort()
print(Country)
Country.sort(reverse=True)
print(Country)
print(len(Country))

# C.71
pizzas = ['Margрarita', 'Pepparoni', 'Marinara']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza} pizza")
print('I really love pizza!')

# C.75
for Number1 in range(1, 21):
    print(Number1)

Number2 = list(range(1, 1_000_001))
print(min(Number2))
print(max(Number2))
print(sum(Number2))

for Number3 in list(range(1, 20, 2)):
    print(Number3)

for Number4 in list(range(3, 31, 3)):
    print(Number4)

Number5 = []
for value in range(1, 11):
    Number5.append(value**3)
    print(Number5)

Number6 = [value**3 for value in range(1, 11)]
print(Number6)

# C.79
print(Country)
print('The irst three items in the list are:')
print(Country[0:3])
print('Three items from the middle of the list are:')
print(Country[1:4])
print('The last three items in the list are:')
print(Country[-3:])

pizzas = ['Margрarita', 'Pepparoni', 'Marinara']
friend_pizzas = pizzas[:]
pizzas.append('Coca')
friend_pizzas.append('Hopa')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# C.82
manus = ('Borsch', 'Lazfnia', 'Jelly', 'Lard', 'Soup')
for manu in manus:
    print(manu)

manus = ('Borsch', 'Lazfnia', 'Jelly', 'A', 'B')
for manu in manus:
    print(manu[0:])

# C.93
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'subaru'? I predict True.")
print(car == 'audi')

car = ['audi', 'bmw', 'toyota', 'subaru']
print(car == 'audi')

car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

print(2 + 3 == 5)
print(18-843 == 3)

print(1982 != 8328)
print(23 + 23 != 46)

print(85 > 24)
print(85 > 102)
print(23 < 34)
print(23 < 12)
print(67 >= 67)
print(67 >= 234)
print(54 <= 54)
print(54 <= 12)

AB1 = 37
AB2 = 86
print(AB1 == 43 and AB2 == 86)
print(AB1 >= 9 and AB2 <= 1927)
print(AB1 >= 45 or AB1 >= 1)
print(AB1 <= 36 or AB2 >= 123)

car = ['audi', 'bmw', 'toyota', 'subaru']
print("bmw" in car)
print('jgk' in car)

# C.99
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('you have earned 5 points')
if 'ifdklc' in alien_color:
    print('jedfewjfi')

alien = ['green']
if 'green' in alien:
    print('you have earned 5 points')
else:
    print('you have earned 10 points')

alien = ['yellow', 'red']
if 'green' in alien:
    print('you have earned 5 points')
else:
    print('you have earned 10 points')

alien = ['green']
if 'green' in alien:
    print('you have earned 5 points')
elif 'yellow' in alien:
    print('you have earned 10 points')
else:
    print('you have earned 15 points')

alien = ['yellow']
if 'green' in alien:
    print('you have earned 5 points')
elif 'yellow' in alien:
    print('you have earned 10 points')
else:
    print('you have earned 15 points')

alien = ['red']
if 'green' in alien:
    print('you have earned 5 points')
elif 'yellow' in alien:
    print('you have earned 10 points')
else:
    print('you have earned 15 points')

age = 58
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('old man')

favorite_fruits = ['banana', 'orange', 'apple']
if 'banana' in favorite_fruits:
    print('You really like banana!')
if 'pear' in favorite_fruits:
    print('You really like pear!')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'pineapple' in favorite_fruits:
    print('You really like pineapple!')

# C.103
names = ['Vova', 'Ivan', 'Admin', 'Katia', 'Oksana']
for name in names:
    if name == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

names = []
if names:
    print("no")
else:
    print("We need to ind some users!")

current_users = ['Vova', 'Ivan', 'Admin', 'Katia', 'Oksana']
new_users = ['Jem', 'Ivan', 'Katia', 'Igor', 'Kolia']
for current_user in current_users:
    if current_user in new_users:
        print('this name is taken, please choose another')
    else:
        print('this name is available')