from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self):
        super().__init__()

    def driver_curent_url(self, url):
        self.driver.get(url)  # порівняння урла який використовуемо для тестів
        sleep(1)
        return self.driver.current_url

    def driver_get_text_h2(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        h2 = self.driver.find_element(By.XPATH, value=".//h2[text()='Jak Wybrać Najlepsze Polskie Sloty?']")
        h2_text = h2  # знаходемо за допомогою XPATH h2 в контенті
        sleep(2)
        return h2_text

    def driver_skrol_to_heder(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        for _ in range (3):
            self.driver.find_element(By.XPATH, value=".//body").send_keys(Keys.PAGE_DOWN)
        #за домомогою рендж прокручую сторінку три рази вниз щоб побачити що зьявляется кнопрка skrol_up
         sleep(2)
        skrol_up = self.driver.find_element(By.XPATH, value=".//div[@class='scroll is_scrolledBox']")
        skrol_up.click()    #знаходемо кнопку skrol_up та за допомогою click піднімаемося до хедера.
        sleep(2)
        return skrol_up

    def driver_ref_butom_ice_casino(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        ref_butom = self.driver.find_element(By.XPATH, value=".//a[@href='/goto/icecasino/']")
        ref_butom.click() #знаходемо рефку /goto/icecasino/ і клікаемо на неї
        sleep(2)
    #ця рефка /goto/icecasino/ веде на два різних урла з різними картинками но в ціх урлах основа одна
    #https: // my - promo7.com / ice_50fs_reg / index.php?ref = sn_w104543c103960l14188gnlp1410_polski - sloty.com
    #https: // my - promo7.com / ice_50fs / index.php?ref = sn_w104543c103960l12858gnlp1410_polski - sloty.com
    # порівнюю частину урла яка не змінюется для цого роблю зміную redirect_url
        redirect_url = "my-promo7.com/ice_50fs"
        sleep(2)
        return redirect_url

    def driver_butom_to_kasyna_online(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        butom_to_kasyna = self.driver.find_element(By.XPATH, value="//a[contains(.,'Lista Online Kasyn')]")
        sleep(2)
        butom_to_kasyna.click()  # знаходемо кнопку з перехідом на сторінку kasyna-online
        sleep(2)
        page_kasyna = self.driver.find_element(By.XPATH, value="//h2[@class='h2'][contains(.,'Lista Polskich Kasyn Online')]")
        sleep(2)# шукаемо h2 таблиці на сторінці kasyna-online
        return page_kasyna.text


    def driver_butom_to_page_GG_Bet(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        butom_to_sloti = self.driver.find_element(By.XPATH, value="//a[contains(.,'GG Bet Opinie')]")
        butom_to_sloti.click()
        sleep(2)   #знаходемо кнопку з перехідом на сторінку sloty-za-darmo
        page_sloti = self.driver.find_element(By.XPATH, value=".//h1") # шукаемо h1 на сторінці sloty-za-darmo
        sleep(2)
        if page_sloti.text != "GG Bet Opinie – Recenzja Kasyna Online":
            return print("Це не сторінка polski-sloty.com/gg-bet/")
            # тут за допомогою If як що h1 відрізняется то вертаемо текст з прінта
        to_main_page = self.driver.find_element(By.XPATH, value=".//img[@class='no-lazy' and @alt='polski sloty logo']")
        to_main_page.click()  # шукаемо по XPATH логотип с рефкой и клікаем на нього, щоб перейти на головну сторінку
        sleep(2)
        page_main = self.driver.find_element(By.XPATH, value=".//h1") # шукаемо h1 на головній
        sleep(2)
        return page_main.text

    def driver_search_butom_list(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        butom_search = self.driver.find_element(By.XPATH, value="//input[contains(@id,'search-input')]")
        sleep(2)
        butom_search.click()
        sleep(2)
        butom_search.clear()
        sleep(2)
        butom_search.send_keys("Book of")
        sleep(2)
        butom_search.send_keys(Keys.ENTER)
        sleep(2) # тут все що робили на занятті добавив тількі пошук по одному із слотів
        page_search = self.driver.find_element(By.XPATH, value="//div[@class='title-slots'][contains(.,'Book of Ra 10')]")
        return page_search.text
