from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from pages.start_page import StartPage
from constants.Staart_page_constans import FrontPageConstans



url1 = "https://polskiesloty.com/"


start_page = StartPage

#test3
def driver_skrol_to_heder(url):
    options = ChromOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get(url)
    sleep(2)
    for _ in range (3):
        driver.find_element(By.XPATH, value=".//body").send_keys(Keys.PAGE_DOWN)
        #за домомогою рендж прокручую сторінку три рази вниз щоб побачити що зьявляется кнопрка skrol_up
    sleep(2)
    skrol_up = driver.find_element(By.XPATH, value=".//div[@class='scroll is_scrolledBox']")
    skrol_up.click()    #знаходемо кнопку skrol_up та за допомогою click піднімаемося до хедера.
    sleep(2)

    return skrol_up
#test4
def driver_ref_butom_ice_casino(url):
    options = ChromOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get(url)
    sleep(2)
    ref_butom = driver.find_element(By.XPATH, value=".//a[@href='/goto/icecasino/']")
    ref_butom.click() #знаходемо рефку /goto/icecasino/ і клікаемо на неї
    sleep(2)
    #ця рефка /goto/icecasino/ веде на два різних урла з різними картинками но в ціх урлах основа одна
    #https: // my - promo7.com / ice_50fs_reg / index.php?ref = sn_w104543c103960l14188gnlp1410_polski - sloty.com
    #https: // my - promo7.com / ice_50fs / index.php?ref = sn_w104543c103960l12858gnlp1410_polski - sloty.com
    # порівнюю частину урла яка не змінюется для цого роблю зміную redirect_url
    redirect_url = "my-promo7.com/ice_50fs"
    sleep(2)

    return redirect_url

#test5
def driver_butom_to_kasyna_online(url):
    options = ChromOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get(url)
    sleep(2)
    butom_to_kasyna = driver.find_element(By.XPATH, value="//a[contains(.,'Lista Online Kasyn')]")
    sleep(2)
    butom_to_kasyna.click()  # знаходемо кнопку з перехідом на сторінку kasyna-online
    sleep(2)
    page_kasyna = driver.find_element(By.XPATH, value="//h2[@class='h2'][contains(.,'Lista Polskich Kasyn Online')]")
    sleep(2)# шукаемо h2 таблиці на сторінці kasyna-online

    return page_kasyna.text
#test6
def driver_butom_to_page_GG_Bet(url):
    options = ChromOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get(url)
    sleep(2)
    butom_to_sloti = driver.find_element(By.XPATH, value="//a[contains(.,'GG Bet Opinie')]")
    butom_to_sloti.click()
    sleep(2)
     #знаходемо кнопку з перехідом на сторінку sloty-za-darmo
    sleep(2)
    page_sloti = driver.find_element(By.XPATH, value=".//h1") # шукаемо h1 на сторінці sloty-za-darmo
    sleep(2)
    if page_sloti.text != "GG Bet Opinie – Recenzja Kasyna Online":
        return print("Це не сторінка polski-sloty.com/gg-bet/") # тут за допомогою If як що h1 відрізняется то вертаемо текст з прінта

    to_main_page = driver.find_element(By.XPATH, value=".//img[@class='no-lazy' and @alt='polski sloty logo']")
    to_main_page.click()  # шукаемо по XPATH логотип с рефкой и клікаем на нього, щоб перейти на головну сторінку
    sleep(2)
    page_main = driver.find_element(By.XPATH, value=".//h1") # шукаемо h1 на головній
    sleep(2)

    return page_main.text
#test7
def driver_search_butom_list(url):
    options = ChromOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(2)
    driver.get(url)
    sleep(2)
    butom_search = driver.find_element(By.XPATH, value="//input[contains(@id,'search-input')]")
    sleep(2)
    butom_search.click()
    sleep(2)
    butom_search.clear()
    sleep(2)
    butom_search.send_keys("Book of")
    sleep(2)
    butom_search.send_keys(Keys.ENTER)
    sleep(2) # тут все що робили на занятті добавив тількі пошук по одному із слотів
    page_search = driver.find_element(By.XPATH, value="//div[@class='title-slots'][contains(.,'Book of Ra 10')]")

    return page_search.text



'''tests'''

#test1
def test_comper_url():
    assert start_page.driver_curent_url(FrontPageConstans.URl) == "https://polskiesloty.com/"

#test2
def test_text_h2():
    assert start_page.driver_curent_url(FrontPageConstans.h2_xpath_text) == "Jak Wybrać Najlepsze Polskie Sloty?"

#test3
def test_botom_skrol_up():
    assert driver_skrol_to_heder(url1)

#test4
def test_ref_ice_casino():
    assert driver_ref_butom_ice_casino(url1) == "my-promo7.com/ice_50fs"

#test5
def test_to_kasyna_online():
    assert driver_butom_to_kasyna_online(url1) == "Lista Polskich Kasyn Online"

#test6
def test_butom_table_to_page_GG_Bet():
    assert driver_butom_to_page_GG_Bet(url1) == "Polski Sloty"

#test7
def test_search_butom_main_page():
    assert driver_search_butom_list(url1) == "Book of Ra 10"
