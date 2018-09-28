def make_car(pruductor, car_type, **else_info):
	info = {}
	info['productor'] = pruductor
	info['car_type'] = car_type
	for k, v in else_info.items():
		info[k] = v
	return info
	
