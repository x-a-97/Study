voited = {}
def check_voter(name):
	if voted.get(name):
		print("kick them out!")
	else:
		voted[name] = True
		print("let them vote!")


# 缓存
cache = {}
def get_page(url):
	if cache.get(url):
		return cache[url]
	else:
		data = get_data_from_server[url]
		cache[url] = data
		return data

