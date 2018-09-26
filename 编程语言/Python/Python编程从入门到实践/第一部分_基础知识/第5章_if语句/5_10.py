current_users = ['admin', 'wuyun', 'zhenhua', 'lg', 'wuping', 'yanjun']
new_users = ['admin', 'wuyun', 'rongying', 'LG', 'yonghua', 'yanjun']

tmp_current_users = []
for current_user in current_users:
	tmp_current_users.append(current_user.lower())
	 	
for new_user in new_users:
	if (new_user.lower() in tmp_current_users):
		print(new_user + " is used")
	else:
		print(new_user + " is ok")
