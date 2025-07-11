name = input("Enter your name: ")
hobby = input("What's your favorite hobby?")
print(f"{name}, it's really cool that you like {hobby}!")
mood = input("How are you feeling today?")
mood = mood.lower()
if mood == "happy":
	print(f"Awesome! Let's keep up the happy vibes :D")
elif mood == "sad":
	print(f"That sucks! Take care of yourself.")
else:
	print(f"Wackyyy bro!")
print(f"Before you get back to the grind, {name}, be sure to take some time for yourself. Whether you're feeling {mood} or wackadoodle, a little {hobby} won't hurt!")
