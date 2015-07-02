#seleniumというブラウザを操作できるモジュールを使用。
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

output_file_dir = './test.text' #出力先
output_file = open(output_file_dir,'w')
search_word = '機械学習'
book_data = [] #書籍情報(Book_dataインスタンス)のリスト

#本のタイトルとリンクを紐付けの為及び汎用性向上のためクラスを作成
class Book_data():
    instance_count = 0 #インスタンスの数をしめす
    def __init__(self,data,output):
        self.no = self.next()
        self.name ,self.link = self.extract_data(data)
        self.write_file(output)
    @classmethod
    def next(cls):#インスタンスのカウント
        cls.instance_count +=1
        return cls.instance_count
    def extract_data(self,data):
        #リンクの抽出
        tmp = data.split("""','1');"><strong>""")
        book_link = 'https://opac.icu.ac.jp' + tmp[0]
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
        file.write('No:'+str(self.no)+'\n')
        file.write('Name:'+self.name+'\n')
        file.write('Link:'+self.link+'\n')
        file.write('\n')

#ドライバーの場所、ドライバーは各々でダウンロードして用意
driver_dir = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(driver_dir) #クローム用のドライバー呼び出し。
driver.get("http://www-lib.icu.ac.jp/")
driver.find_element_by_name('kywd').send_keys(search_word)
driver.find_element_by_name('kywd').send_keys(Keys.RETURN)
driver.close()
driver.switch_to.window("opac") #検索結果を表示したウインドウに移動。
html = driver.page_source #HTMLの取得


#データの整形:必要のないHTMLコードの上部分を除去
html_cut_head = html.split('<div id="main_list">',1)
#データの整形:必要のないHTMLコードの下部分を除去
html_cut_last = html_cut_head[1].split('</div><div class="link_block">',1)
#本のデータを塊ごとをリストに入れる
data = html_cut_last[0].split("""<a href="javascript:DisplayWindow('""")

#本のデータをクラスに入れる。
for n in range(1,len(data)):
    book_data.append(Book_data(data[n],output_file))

output_file.close() #ファイルを閉じる。
driver.close() #ウインドウを閉じる

#データの出力
for n in range(len(book_data)):
    book_data[n].show_info()
