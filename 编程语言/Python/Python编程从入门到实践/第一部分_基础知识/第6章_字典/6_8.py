coco = {
	'type' : 'rabbit',
	'master' : 'zhb',
}
lucky = {
	'type' : 'dog',
	'master' : 'zx',
}
sci = {
	'type' : 'bird',
	'master' : 'zhb',
}

pets = [coco, lucky, sci]

for pet in pets:
	for k,v in pet.items():
		print(k + ":" + v)
