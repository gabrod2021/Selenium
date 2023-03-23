from selenium import webdriver
from selenium.webdriver.support.ui import  Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C://Users/User/OneDrive/Escritorio/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(executable_path=path)
driver.get(website)

#CON PATH ABSOLUTO-(mas propenso a errores con los cambios)
#all_matches_button = driver.find_element("xpath",'//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')

#CON PATH RELATIVO-(mas conveniente y mas corto)
all_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown=Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

time.sleep(5)

matches=driver.find_elements_by_tag_name('tr')


partidos=[]
for match in matches:
    #print(match.text)
    partidos.append(match.text)

driver.quit()

#Pandas
df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)