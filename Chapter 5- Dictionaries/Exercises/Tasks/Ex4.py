major_rivers = {
    'Rio Grande': 'USA',
    'Ganges River': 'India',
    'Pearl River': 'China',
    }

for river,country in major_rivers.items():
    print("River " + river.title()+ " runs through "+ country.title() +".")
print("\nIncluded Rivers:")
for river in major_rivers.keys():
    print("*" + river.title())

print("\nIncluded Coutries:")
for country in major_rivers.values():
    print("*" + country.title())