from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
driver = webdriver.Firefox()
driver.get('http://www-lib.icu.ac.jp/')
driver.find_element_by_name('kywd').send_keys('機械学習')
driver.find_element_by_name('kywd').send_keys(Keys.RETURN)
#driver.find_element_by_name('kywd1').submit()
#driver.save_screenshot("ss.png")
driver.close()
driver.switch_to.window("opac")
name = driver.find_elements_by_class_name('name')
html = driver.page_source
#driver.close()
#print(html.encode('utf8'))
#str(html) = html
data = html.split('<td class="list_result">',1)
book = data[1].split('</div><div class="link_block">',1)
book2 = book[0].split('<span class="name">')
#print(book[0].encode('utf8'))
for m in book2:
    m2 = m.split('>',1)
    print(m2[0].encode('utf8'))
for n in name:
    book = n.text.split("/")
    print(book[0])
print('Chose Title')
s = input('--> ')

driver.close()
