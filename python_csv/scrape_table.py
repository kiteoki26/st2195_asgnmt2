#Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Request url
url = "https://en.wikipedia.org/wiki/Comma-separated_values"
page = requests.get(url)

#Fetch webpage
soup = BeautifulSoup(page.content, "html.parser")

#Scraping data
#Year #Make #Model #Description #Price
table = soup.find("table", {"class":"wikitable"})

colYear = []
colMake = []
colModel = []
colDesc = []
colPrice = []


for x in table: 
    rows = table.find_all('tr')
    
for row in rows:
    cells = row.find_all('td')

    if len(cells) > 1 :
            
        year = cells[0]
        colYear.append(int(year.text))
        
        make = cells[1]
        colMake.append(make.text)
        
        model = cells[2]
        colModel.append(model.text)
        
        desc = cells[3]
        colDesc.append(desc.text)
        
        price = cells[4]
        colPrice.append(float(price.text))


df = pd.DataFrame(colYear, index=None, columns = ['Year']) 
df['Make'] = colMake
df['Model'] = colModel
df['Description'] = colDesc
df['Price'] = colPrice

df.to_csv('python_car_table.csv', index = False)