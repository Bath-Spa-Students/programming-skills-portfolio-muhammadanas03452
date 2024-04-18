sandwich_orders = ["Grilled Chiken","pastrami", "Molten Cheese","pastrami", "club sandwich", "Ham","pastrami"]
finished_sandwiches = []


print("Sorry we are out of Pastrami!")
while 'pastrami' in sandwich_orders:
   sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
  print(f"I made {sandwich} sandwich for you.")
  finished_sandwiches.append(sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
