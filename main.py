from Dog import Dog


codie = Dog('Codie', 12, 20)
jackson = Dog('Jackson', 12, 20)
fred = Dog('Fred', 12, 20)
zero = Dog('Zero')

print(zero)

my_dogs = [codie, jackson, fred, zero]
for dog in my_dogs:
    print(dog)

my_dogs.sort()
print("\n\nSorted\n")
for dog in my_dogs:
    print(dog)

my_dogs.sort(reverse=True)
print("\n\nReversed\n")
for dog in my_dogs:
    print(dog)

