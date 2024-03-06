from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credetials import USERNAME, PASSWORD
from bs4 import BeautifulSoup 
import time

# Creating a webdriver instance
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options = chrome_options)
driver.fullscreen_window()
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://www.linkedin.com/")

# waiting for the page to load


# entering username
username = driver.find_element(By.ID, "session_key")
driver.implicitly_wait(3)
# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys(USERNAME) 

# entering password
pword = driver.find_element(By.ID, "session_password")
driver.implicitly_wait(3)

# In case of an error, try changing the element 
# tag used here.

# Enter Your Password
pword.send_keys(PASSWORD)	 
driver.implicitly_wait(3)

# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
# //*[@id="global-nav-search"]/div
search_button = driver.find_element(By.XPATH,'//*[@id="global-nav-search"]/div')
driver.implicitly_wait(3)
search_button.click()


search = driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
driver.implicitly_wait(3)
search.clear()
search.click()
search.send_keys('automation in IT')
time.sleep(2)
search.send_keys(Keys.RETURN)

#TODO - get posts

time.sleep(5)
current_url = driver.current_url
posts_url = current_url.replace('all', 'content',1)
driver.get(posts_url)

page_source = driver.page_source
file_ps = open('page_source.txt','w',encoding='utf-8')
# print(page_source)
# test = page_source.__str__
file_ps.write(page_source)
soup = BeautifulSoup(page_source, features="html.parser")
soup_txt = open('soup_post.txt','w',encoding='utf-8')
soup_txt.write(soup.prettify())

content = soup.find_all('div',{'class': 'update-components-article'})
print(content)


driver.get('https://www.linkedin.com/m/logout')



time.sleep(3)
driver.quit()