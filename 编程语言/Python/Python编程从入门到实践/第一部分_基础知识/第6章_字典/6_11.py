beijing = {
	'country' : 'china',
	'population' : '1234567',
	'fact' : 'shoudu',
}

shanghai = {
	'country' : 'china',
	'population' : '999999',
	'fact' : 'modu',
}

shenzhen = {
	'country' : 'china',
	'population' : '22222',
	'fact' : 'chuangxin',
}

cities = {
	'beijing':beijing,
	'shanghai':shanghai,
	'shenzhen':shenzhen,
}

for k,v in cities.items():
	print(k+":")
	for m,n in v.items():
		print(m + ":" + n)
	print()

