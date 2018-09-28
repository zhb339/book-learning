def make_album(singer, album, num = []):
	alb = {singer : album}
	if num:
		alb['num'] = num
	return alb
	
print(make_album('asam', 'song'))
print(make_album('wuyuetian', 'aiqingwansui', 6))
