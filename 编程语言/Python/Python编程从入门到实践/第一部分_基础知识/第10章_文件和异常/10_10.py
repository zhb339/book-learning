def count_file(filename, word):
	with open(filename) as fobj:
		txt = fobj.read()
		print(txt.count(word))
count_file('10_9.py', 'print')
