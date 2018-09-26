zhouxuan = {
	'name' : 'xuan',
	'first' : 'zhou',
	'city' : 'fuzhou',
	'age' : 29,
}

chenxin = {
	'name' : 'xin',
	'first' : 'chen',
	'city' : 'fuzhou',
	'age' : 29,
}

wangwei = {
	'name' : 'wei',
	'first' : 'wang',
	'city' : 'fuzhou',
	'age' : 29,
}
people = [zhouxuan, chenxin, wangwei]

for girl in people:
	for k,v in girl.items():
		print(k + ":" + str(v))
	print("\n")

