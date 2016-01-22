import requests as req
import re

box = []
baseUrl = "http://www.sohu.com/"
def getUrls(text):
	result = re.findall(r'href="(.*?)"',text)
	#print(result)
	return result
	

	#"http://www.ximalaya.com/"+result[0]
def Fetched(url):
	if url not in box:
		box.append(url)
		return False
	return True

def wide(url):
	try:
		text = req.get(url).text
		while not Fetched(url):
			#print(text)
			next = getUrls(text)
			print(url)
			for i in next:
				wide(url)
	except:
		print('ooo')

wide(baseUrl)