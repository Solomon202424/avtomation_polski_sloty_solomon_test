from time import sleep

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
