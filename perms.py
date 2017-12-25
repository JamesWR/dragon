
def makedig(num, place):
	return num*(10**place)
	

def perms(max):
	permlist = []
	
	
def recperms(max, loc, used):
	list = []
	for i in range(max):
		if i not in used:
			for num in recperms(max, loc-1, used+[i]):
				list.append(num+makedig(i,loc))
	return list;