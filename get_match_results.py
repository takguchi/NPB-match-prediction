from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

# ブラウザのオプションを格納する変数を取得する
options = Options()
# Headlessモードを有効にする
# →コメントアウトするとブラウザが実際に立ち上がる
options.set_headless(True)
# ブラウザを起動する
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
# ブラウザでアクセスする
driver.get("http://baseballdata.jp/2017/376/GResult.html")
# 「全て見る」リンクを押下して全データを表示させる
driver.find_element_by_class_name('allshow').click()
sleep(1)
# HTMLの文字コードをUTF-8に変換して取得する
html = driver.page_source.encode('utf-8')

bsObj = BeautifulSoup(html,"html.parser")
rows = bsObj.findAll("tr")

# CSVファイルの設定
csvFile = open("csv/2017_E_match_results.csv",'wt', newline = '', encoding = 'utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll("td"):
            csvRow.append(cell.get_text().strip())
        writer.writerow(csvRow)
finally:
    csvFile.close()
