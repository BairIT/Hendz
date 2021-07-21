import select
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import bs4
import re
import time
##########Begin
url_1 = 'http://home.hendz.ru/overtime/logon'
driver = webdriver.Firefox(executable_path='/home/bair/PycharmProjects/pythonProject1/geckodriver')
driver.get(url_1)
loginuser = driver.find_element_by_id('userlogin')
loginpass = driver.find_element_by_id('userpass')
loginuser.send_keys("b.imigeev")
loginpass.send_keys("123456")
#задержка ввода логина и пароля 1c
time.sleep(1)
autorizz = driver.find_element_by_id('autoriz')
autorizz.click()
# задержка 1c
time.sleep(1)
add = driver.find_element_by_link_text('Добавить отчёт')
add.click()
# Задержка 1c
time.sleep(1)
spisok_id = []
spisok_date = []
spisok_adress = []
with open('/home/bair/PycharmProjects/pythonProject3/1.html') as file:
     src = file.read()
     soup = bs4.BeautifulSoup(src)
     for i in soup:
         all_td = soup.findAll('td',headers="col_1")
         spisok_id = list(all_td)
         all_date = soup.findAll('td',headers="col_4")
         spisok_date = list(all_date)
         all_adress = soup.findAll('td',headers="col_7")
         spisok_adress = list(all_adress)
a = []
b = []
c = []
for h in spisok_id:
    g = list(h)
    str_id = str(g)
    str_id = str_id.strip('[')
    str_id = str_id.strip(']')
    str_id = str_id.strip("'")
    a.append(str_id)
for l in spisok_date:
    d = list(l)
    str_dat = str(d)
    str_dat = str_dat.strip('[')
    str_dat = str_dat.strip(']')
    str_dat = str_dat.strip("'")
    b.append(str_dat)
for m in spisok_adress:
     j = list(m)
     str_addr = str(j)
     str_addr_2 = re.sub(r'\s+',' ',str_addr)
     str_addr_3 = re.sub(r'\\n','',str_addr_2)
     str_addr_4 = re.sub(r'\\\\',' ',str_addr_3)
     str_addr_4 = str_addr_4.strip('[')
     str_addr_4 = str_addr_4.strip(']')
     str_addr_4 = str_addr_4.strip("'")
     c.append(str_addr_4)
count = 0
for i3,index in enumerate(c):
  stop1 = False
  stop2 = False
  time.sleep(2)
  adresssub = driver.find_element_by_name('adressub')
  adresssub.send_keys(c[i3])
  for i2,index1 in enumerate(b):
      if stop1:
          break
      else:
        i2=i3
        bb = str(b[i2])
        bbb = int(bb[:2])
        Select(driver.find_element_by_name('subd')).select_by_index(bbb)
        etamsk = driver.find_element_by_name('etamsk')
        etamsk.send_keys(b[i2])
        Select(driver.find_element_by_id('vidz')).select_by_index(4)
        Select(driver.find_element_by_name('suby')).select_by_index(2)
        Select(driver.find_element_by_name('subm')).select_by_index(6)
        kmsub = driver.find_element_by_name('kmsub')
        kmsub.send_keys(0)
        Select(driver.find_element_by_name('klient')).select_by_index(6)
        discsub = driver.find_element_by_name('discsub')
        discsub.send_keys('выполнено')
        for i1,index2 in enumerate(a):
            if stop2:
                break
            else:
                numberZ = driver.find_element_by_name('nza')
                i1=i3
                numberZ.send_keys(a[i1])
                injiaddz = driver.find_element_by_id('injiaddz')
                injiaddz.click()
                time.sleep(1)
                if count == len(c):
                    print('The END!!!Congratilations!!!')
                    exit()
                else:
                    stop1 = True
                    stop2 = True
                    add = driver.find_element_by_link_text('Добавить отчёт')
                    add.click()
                    count += 1
                    print(a[i1])
                    print(b[i2])
                    print(c[i3])







