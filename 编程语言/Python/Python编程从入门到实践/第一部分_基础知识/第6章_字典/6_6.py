favorite_language = {
	"zhb":'Python',
	"liugang":'VHDL',
	"wuyun":'Java',
	"rongying":'Go',
	"zhenhua":'Python',	
}

names = ['zhb', 'yonghua', 'wuyun']

for name in names:
	if name in favorite_language.keys():
		print("Thank you " + name + " for coming")
	else:
		print(name + " please com!")
