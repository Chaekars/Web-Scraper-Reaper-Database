import requests as uReq
from bs4 import BeautifulSoup as soup
import time

my_url = 'http://www.reapermini.com/OnlineStore/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

sets = ['Bones','Chronoscope','Pathfinder','SavageWorlds','DarkHeavenLegends','Base']
init = [77,800,890,590,0,740]
first = [1,1,1,1,2001,1]
last = [640,86,43,49,3903,59]

for setVal in range(0,6):
	print("Importing: " + sets[setVal])
	file = open(("Unprocessed\\" + (sets[setVal] + ".dat")),"w")
	for val in range(first[setVal],last[setVal]):
		ID = (str)(init[setVal])
		try:
			while len(ID)+len((str)(val)) < 5:
				ID = ID + '0'
			ID = ID + (str)(val)
			temp_url = my_url + sets[setVal] + '/latest/' + ID
			page = uReq.get(temp_url)
			page_soup = soup(page.text,"html.parser")
			tablesBox = page_soup.findAll("table",{"border":"0"})
			textVal = tablesBox[3].findAll("td",{"valign":"top"})
			print(val)
			file.write(textVal[1].text.strip() + "\n")
		except:
			print(ID + ' not saved to data')
		time.sleep(1)
	print("Import for " + sets[setVal] + "Completed")
	file.close()
print("All Imports Done")