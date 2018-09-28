while (True):
	name = input("Please enter your name: ")
	print(name)
	with open("guest_book.txt", 'a') as txt_obj:
		txt_obj.write(name + ' coming \n')
