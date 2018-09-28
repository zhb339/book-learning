while (True):
	reason = input("Please enter the reason of coding: ")
	with open("reason.txt", 'a') as txt_obj:
		txt_obj.write(reason + '\n')
