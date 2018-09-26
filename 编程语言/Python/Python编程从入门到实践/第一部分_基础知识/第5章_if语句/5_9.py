users = []

if (users == []):
	print("We need to find some users")

for user in users:
	if (user == 'admin'):
		print("Hello admin, would like to see a status report")
	else:
		print("Hello " + user + " thank you for logging")
