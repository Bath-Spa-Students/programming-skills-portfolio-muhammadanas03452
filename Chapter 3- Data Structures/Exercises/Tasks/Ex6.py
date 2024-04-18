guests_dinner = ['Michael','James','Issac newton']
print("I'm Sorry, but I can only invite two people for dinner")
while len(guests_dinner)>2:
    guests = guests_dinner.pop()
print("Sorry",guests + " I can't invite you at dinner this time")

for guests in guests_dinner:
    print("Dear", guests +"," + " cordially invited to join me for a delightful evening of dinner")
