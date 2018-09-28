with open('learning_python.txt') as lobj:
	content1 = lobj.read()
print(content1)

print()

with open('learning_python.txt') as lobj:
	for line in lobj:
		print(line.strip())

print()
with open('learning_python.txt') as lobj:
	lines = lobj.readlines()
for line in lines:
	print(line.strip())
