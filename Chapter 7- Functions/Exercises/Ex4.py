def make_shirt(size="large", message="I love Python!"):
 
  print(f"We're making a {size} shirt with printed text: {message}")

# Call the function with various arguments
make_shirt() #default
make_shirt(size="medium")  # Medium
make_shirt(message="I love kittens", size="small")  # Small