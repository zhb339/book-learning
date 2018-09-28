def user_profile(first_name, last_name, **user_info):
	profile = {}
	profile['first'] = first_name
	profile['last'] = last_name
	for k, v in user_info.items():
		profile[k] = v
	return profile
	
print(user_profile('zheng', 'hongbo', country = 'china', work = 'IT', school = 'UESTC'))
