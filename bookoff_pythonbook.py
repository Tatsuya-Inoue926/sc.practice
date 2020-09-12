from selenium import webdriver
from time import sleep
import csv
import datetime


browser = webdriver.Chrome( executable_path = "C:\\Users\\ユーザー\\Desktop\\Mypandas\\chromedriver.exe")
browser.implicitly_wait(3)

sleep(3)
url = "https://www.bookoffonline.co.jp/display/L001,p=1,sk=10,st=a,q=python"
browser.get(url)

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = ("bookoff_python_data" + csv_date + ".csv")
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")


writer = csv.writer(f, lineterminator="\n") 
csv_header = ["タイトル","価格(中古）", "発売年月日(その他詳細）"]
writer.writerow(csv_header)

sleep(10)
for elem_n, elem_p, elem_t in zip(browser.find_elements_by_class_name("itemttl"), browser.find_elements_by_class_name("mainprice"), browser.find_elements_by_class_name("spec")):
    print(elem_n.text, elem_p.text, elem_t.text)
    csvlist = []
    csvlist.append( elem_n.text)
    csvlist.append( elem_p.text)
    csvlist.append( elem_t.text)
    writer.writerow(csvlist)


next_link = browser.find_element_by_css_selector("#resList > form > div:nth-child(1) > div.numNavi > a:nth-child(5)")
browser.get(next_link.get_attribute("href"))


i = 0
while True:
    i += 1
    sleep(10)
    for elem_n, elem_p, elem_t  in zip(browser.find_elements_by_class_name("itemttl"), browser.find_elements_by_class_name("mainprice"), browser.find_elements_by_class_name("spec")):
        print(elem_n.text, elem_p.text, elem_t.text)
        csvlist=[]
        csvlist.append(elem_n.text)
        csvlist.append(elem_p.text)
        csvlist.append(elem_t.text)
        writer.writerow(csvlist)
    next_link = browser.find_element_by_css_selector("#resList > form > div:nth-child(1) > div.numNavi > a:nth-child(6)")
    browser.get(next_link.get_attribute("href"))
    if i > 3:
        break

f.close()
browser.close()
