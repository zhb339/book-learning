def show_magicians(names):
	for name in names:
		print(name)
	print()

def make_great(names):
	new_names = []
	for name in names:		
		new_names.append("the Great " + name)
	while names:
		names.pop()
	while new_names:
		names.append(new_names.pop())
	return names

magician_names = ['david', 'jack', 'lilei']

make_great(magician_names)

show_magicians(magician_names)
