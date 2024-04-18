destinations_list = ['Turkey', 'Australia', 'Brazil', 'USA', 'Spain']

print("My travel destinations:")
print(destinations_list)

print("\nDestinations in alphabetical order:")
print(sorted(destinations_list))

print("\nMy travel destinations:")
print(destinations_list)

print("\nReverse alphabetical order:")
print(sorted(destinations_list, reverse=True))

destinations_list.reverse()
print("\nBy reverse():")
print(destinations_list)

destinations_list.reverse()
print("\nBy reverse() again:")
print(destinations_list)

destinations_list.sort()
print("\nBy sort():")
print(destinations_list)

destinations_list.sort(reverse=True)
print("\nBy sort() again:")
print(destinations_list)