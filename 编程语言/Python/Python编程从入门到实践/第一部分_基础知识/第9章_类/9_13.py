from collections import OrderedDict

favorite = OrderedDict()
favorite['C'] = 'The C programming language'
favorite['Python'] = 'A very popular programming language'
favorite['Java'] = 'The most wide used language'
favorite['C++'] = '(Enhanced C)'
favorite['PHP'] = 'The best language'
favorite['C#'] = 'The language of microsoft'

for k,v in favorite.items():
	print(k + ":" + v)
