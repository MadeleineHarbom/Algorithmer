from L1.LivingThings import Dog, Person


print('E1')




ppl = [Person('Madeleine', 'Rudkjøbing'), Person('Malin', 'Solberg'), Person('Mikael', 'Harbom')]

for p in ppl:
    print(p.name())

print('E2')




puppies = [Dog('Patrick'), Dog('Douglas'), Dog('Molly'), Dog('Karla'), Dog('Mini'),
           Dog('Rufus'), Dog('Nemisis'), Dog('Samson')]

for puppy in puppies:
    print(puppy.name())

mixspeces = ppl + puppies

for names in mixspeces:
    print(names.name())

print('E3')
print('Just moving some shit around')
print('E4')
print("While Python classes don't have true private attributes, if an attribute name begins with two underscores,"
      " the Python interpreter internally modifies the attribute's name, "
      "so that references to the attribute will not be resolved")

print('Man kan adgaa private private metoder med __, men lad vaere :P')