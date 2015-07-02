#seleniumというブラウザを操作できるモジュールを使用。
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#本のタイトルとリンクを紐付けの為及び汎用性向上のためクラスを作成
class Book_data():
    instance_count = 0 #インスタンスの数をしめす
    def __init__(self,data):
        self.no = self.next()
        self.name ,self.link = self.extract_data(data)
    @classmethod
    def next(cls):#インスタントのカウント
        cls.instance_count +=1
        return cls.instance_count
    def extract_data(self,data):
        #リンクの抽出
        tmp = data.split('<strong>',1)
        book_link = tmp[0]
        #書籍名の抽出
        tmp2 = tmp[1].split('</strong>',1)
        tmp3 = tmp2[0].split('/',1)
        book_name = tmp3[0]
        return book_name, book_link
    def show_info(self):
        print('No:', self.no)
        print('Name:', self.name)
        print('Link:', self.link)
    def write_file(self,file):
        f.write('No:'+str(self.no)+'\n')
        f.write('Name:'+self.name+'\n')
        f.write('Link:'+self.link+'\n')
        f.write('\n')


f = open('./test.text','w') #カレントディレクトリに結果を出力する。
#クローム用のドライバー呼び出し。ドライバーは各々でダウンロードして用意。
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www-lib.icu.ac.jp/")
driver.find_element_by_name('kywd').send_keys('機械学習')
driver.find_element_by_name('kywd').send_keys(Keys.RETURN)
driver.close()
driver.switch_to.window("opac") #検索結果を表示したウインドウに移動。
html = driver.page_source #HTMLの取得

#データの整形
#必要のないHTMLコードの上部分を除去
html_cut_head = html.split('<div id="main_list">',1)
#必要のないHTMLコードの下部分を除去
html_cut_last = html_cut_head[1].split('</div><div class="link_block">',1)
#本のデータの塊ごとをリストに入れる
data = html_cut_last[0].split('<span class="name">')

book_data = [] #book_dataインスタンスのリスト

#実際にデータをクラスに入れる。
for n in range(1,len(data)):
    book_data.append(Book_data(data[n]))

driver.close() #ウインドウを閉じる

#データの出力
for n in range(len(book_data)):
    book_data[n].write_file(f)
    book_data[n].show_info()

f.close()
