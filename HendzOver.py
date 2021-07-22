import select
import re
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import bs4


def main():
    url_1 = 'http://home.hendz.ru/overtime/logon'
    source_table = '1.html'
    login = "b.imigeev"
    password = "123456"

    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.get(url_1)

    loginuser = driver.find_element_by_id('userlogin')
    loginuser.send_keys(login)

    loginpass = driver.find_element_by_id('userpass')
    loginpass.send_keys(password)

    time.sleep(1)

    autorizz = driver.find_element_by_id('autoriz')
    autorizz.click()

    time.sleep(1)

    add = driver.find_element_by_link_text('Добавить отчёт')
    add.click()

    time.sleep(1)

    with open(source_table) as file:
        src = file.read()
        soup = bs4.BeautifulSoup(src)
        for i in soup:
            ids = list(soup.findAll('td', headers="col_1"))
            dates = list(soup.findAll('td', headers="col_4"))
            addresses = list(soup.findAll('td', headers="col_7"))

    parsed_ids = []
    parsed_dates = []
    parsed_addresses = []

    for uid in ids:
        str_id = str(list(uid))
        str_id = str_id.strip('[')
        str_id = str_id.strip(']')
        str_id = str_id.strip("'")
        parsed_ids.append(str_id)

    for date in dates:
        str_date = str(list(date))
        str_date = str_date.strip('[')
        str_date = str_date.strip(']')
        str_date = str_date.strip("'")
        parsed_dates.append(str_date)

    for address in addresses:
        str_addr = str(list(address))
        str_addr_2 = re.sub(r'\s+', ' ', str_addr)
        str_addr_3 = re.sub(r'\\n', '', str_addr_2)
        str_addr_4 = re.sub(r'\\\\', ' ', str_addr_3)
        str_addr_4 = str_addr_4.strip('[')
        str_addr_4 = str_addr_4.strip(']')
        str_addr_4 = str_addr_4.strip("'")
        parsed_addresses.append(str_addr_4)

    count = 0
    for i3, index in enumerate(parsed_addresses):
        stop1 = False
        stop2 = False

        time.sleep(2)

        adresssub = driver.find_element_by_name('adressub')
        adresssub.send_keys(parsed_addresses[i3])

        for i2, index1 in enumerate(parsed_dates):
            if stop1:
                break
            else:
                i2 = i3

                bb = str(parsed_dates[i2])
                bbb = int(bb[:2])

                Select(driver.find_element_by_name('subd')).select_by_index(bbb)

                etamsk = driver.find_element_by_name('etamsk')
                etamsk.send_keys(parsed_dates[i2])

                Select(driver.find_element_by_id('vidz')).select_by_index(4)
                Select(driver.find_element_by_name('suby')).select_by_index(2)
                Select(driver.find_element_by_name('subm')).select_by_index(6)

                kmsub = driver.find_element_by_name('kmsub')
                kmsub.send_keys(0)

                Select(driver.find_element_by_name('klient')).select_by_index(6)

                discsub = driver.find_element_by_name('discsub')
                discsub.send_keys('выполнено')

                for i1, index2 in enumerate(parsed_ids):
                    if stop2:
                        break
                    else:
                        numberZ = driver.find_element_by_name('nza')
                        i1 = i3
                        numberZ.send_keys(parsed_ids[i1])

                        injiaddz = driver.find_element_by_id('injiaddz')
                        injiaddz.click()

                        time.sleep(1)

                        if count >= len(parsed_addresses):
                            print('The END!!!Congratilations!!!')
                            exit()
                        else:
                            stop1 = True
                            stop2 = True

                            add = driver.find_element_by_link_text('Добавить отчёт')
                            add.click()

                            count += 1

if __name__ == '__main__':
    main()
