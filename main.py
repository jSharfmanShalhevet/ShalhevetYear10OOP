from Dog import Dog



codie = Dog('Codie', 12, 38)
jackson = Dog('Jackson', 10, 18)
fred = Dog('Fred', 5, 20)

my_dogs = [codie, jackson, fred]
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

