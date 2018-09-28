def make_album(singer, album, num = []):
	alb = {singer : album}
	if num:
		alb['num'] = num
	return alb

while (True):
		singer = input("Enter singer name (q to quit): ")
		if (singer == 'q'):
			break
		album = input("Enter album name (q to quit): ")
		if (album == 'q'):
			break
		print(make_album(singer, album))

