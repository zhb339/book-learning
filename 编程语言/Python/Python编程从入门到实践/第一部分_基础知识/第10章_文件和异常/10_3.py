name = input("Please enter your name: ")
with open("guest.txt", 'a') as txt_obj:
	txt_obj.write(name + '\n')
