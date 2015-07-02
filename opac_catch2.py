from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
class Book_data:
    def __init__(self,name,link):
        self.name = name
        self.link = link
    def show_info(self):
        print('Book:', self.name)
        print('Link:', self.link)

f = open('./test.text','w')
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www-lib.icu.ac.jp/")
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
link = data[1].split('</div><div class="link_block">',1)
book_link = link[0].split('<span class="name">')
#print(book[0].encode('utf8'))
#for m in book2:
    #m2 = m.split('>',1)
    #print(m2[0].encode('utf8'))
    #f.write(m2[0]+'\n')
#for n in name:
    #book = n.text.split("/")
    #print(book[0])
    #f.write(book[0]+'\n')
book_data = []
for n in range(len(name)):
    m = book_link[n-1].split('<s',1)
    book_name = name[n].text.split("/")
    print(n, end=' ')
    #print(book_name[0])
    #print(m[0].encode('utf8'))
    f.write(book_name[0]+'\n')
    f.write(m[0]+'\n')
    book_data.append(Book_data(book_name[0], m[0]))
#print('Chose Title')
#s = input('--> ')
#f.write(str(html.encode('utf8')))
for n in range(len(book_data)):
    book_data[n].show_info()
f.close()
driver.close()
