pet1 = {
    'Animal': 'cat',
    'owner': 'Liam'
    }

pet2 = {
    'Animal': 'dog',
    'owner': 'James'
    }

pet3 = {
    'Animal': 'fish',
    'owner': 'john'
    }

pets = [pet1, pet2, pet3]
for pet in pets:
    Animal = pet['Animal'].title()
    owner  = pet['owner'].title()
    print(owner + "'s pet is a " + Animal + ".")