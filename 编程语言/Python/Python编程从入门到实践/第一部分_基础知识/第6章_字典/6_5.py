rivers = {
	'changjiang':'china',
	'huanghe':'china',
	'mingjiang':'fujian',
	'fuchunxi':'ningde',
}

for k,v in rivers.items():
	print(k + " run through " + v)

print("\n")

for k in rivers.keys():
	print(k)

print("\n")

for v in set(rivers.values()):
	print(v)
