def defaultOrder(tribes):
	tribes = list(tribes)
	tribes.sort(key=lambda x: x.created_at, reverse=True)
	return list(tribes)


def orderByNameAsc(tribes):
	tribes = list(tribes)
	tribes.sort(key=lambda x: x.name)
	return tribes


def orderByNameDesc(tribes):
	tribes = list(tribes)
	tribes.sort(key=lambda x: x.name, reverse=True)
	return tribes


def orderByNumOfMembersAsc(tribes):
	tribes = list(tribes)
	tribes.sort(key=lambda x: x.getNumberOfMembers())
	return tribes


def orderByNumOfMembersDesc(tribes):
	tribes = list(tribes)
	tribes.sort(key=lambda x: x.getNumberOfMembers(), reverse=True)
	return tribes