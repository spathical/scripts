
def set_value(d, key):
	s = key.split(".")
	value = d[s[1]]
	for i in s[2:-1]:
		value = value[i]
	print value[s[-1]]
	value[s[-1]] = str(value[s[-1]])


def walk(d, root, t):
    ''' Walk the dict and stringify values '''
    for k, v in d.items():
        if type(v) == t:
		set_value(d, root + '.' + k)
        if type(v) == dict:
		walk(v, root + '.' + k)
        if type(v) == list:
		for i, val in enumerate(v):
			if type(val) == dict:
				walk(val, root + "." + k + "." + str(i))

