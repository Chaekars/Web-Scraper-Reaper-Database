import requests as uReq
from bs4 import BeautifulSoup as soup
import time

my_url = 'http://www.reapermini.com/OnlineStore/Chronoscope/latest/77'
#still needs the last digits

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

file = open("temp.dat","w")

for val in range(1,99):
	temp = ''
	try:
		if val < 10:
			temp = '00'
			temp = (temp + (str)(val))
		else:
			temp = (temp + (str)(val))

		page = uReq.get(my_url + temp)
		page_soup = soup(page.text,"html.parser")
		tablesBox = page_soup.findAll("table",{"border":"0"})
		textVal = tablesBox[3].findAll("td",{"valign":"top"})
		print(val)
		file.write(textVal[1].text.strip() + "\n")
	except:
		print('800' + temp + ' not saved to data')
	time.sleep(1)
print('import finished')
file.close()