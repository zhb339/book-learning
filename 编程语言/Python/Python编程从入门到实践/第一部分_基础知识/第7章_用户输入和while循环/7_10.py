exit_flag = False
places = []
while (exit_flag == False):
	place = input("If you could visit one place in th world, where would you go?")
	places.append(place)
	print("Now you want to go these places")
	for dest in places:
		print(dest)
	print()
