#seleniumというブラウザを操作できるモジュールを使用。
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#本のタイトルとリンクを紐付けの為及び汎用性向上のためクラスを作成
class Book_data:
    def __init__(self,name,link):
        self.name = name
        self.link = link
    def show_info(self):
        print('Book:', self.name)
        print('Link:', self.link)

#カレントディレクトリに結果を出力する。
f = open('./test.text','w')

#クローム用のドライバー呼び出し。ドライバーは各々でダウンロードして用意。
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www-lib.icu.ac.jp/")
driver.find_element_by_name('kywd').send_keys('機械学習')
driver.find_element_by_name('kywd').send_keys(Keys.RETURN)
driver.close()
#検索結果を表示したウインドウに移動。
driver.switch_to.window("opac")
name = driver.find_elements_by_class_name('name')
html = driver.page_source
#データの整形
data = html.split('<td class="list_result">',1)
link = data[1].split('</div><div class="link_block">',1)
book_link = link[0].split('<span class="name">')
#データを収納
book_data = []
for n in range(len(name)):
    m = book_link[n-1].split('<s',1)
    book_name = name[n].text.split("/")
    print(n, end=' ')
    f.write(book_name[0]+'\n')
    f.write(m[0]+'\n')
    book_data.append(Book_data(book_name[0], m[0]))

driver.close()

for n in range(len(book_data)):
    book_data[n].show_info()


f.close()
