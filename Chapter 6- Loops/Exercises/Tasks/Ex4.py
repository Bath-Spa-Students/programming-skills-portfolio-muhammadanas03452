sandwich_orders = ["Grilled Chiken", "Molten Cheese", "club sandwich", "Ham"]
finished_sandwiches = []

for sandwich in sandwich_orders:
  print(f"I made {sandwich} sandwich for you.")
  finished_sandwiches.append(sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
