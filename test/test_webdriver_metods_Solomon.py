from pages.start_page import StartPage
from constants.Start_page_constans import StartPageConstans


start_page = StartPage
'''tests'''

#test1
def test_comper_url():
    assert start_page.driver_curent_url(StartPageConstans.url) == "https://polskiesloty.com/"

#test2
def test_text_h2():
    assert start_page.driver_curent_url(StartPageConstans.url) == "Jak Wybrać Najlepsze Polskie Sloty?"

#test3
def test_botom_skrol_up():
    assert start_page.driver_skrol_to_heder(StartPageConstans.url)

#test4
def test_ref_ice_casino():
    assert start_page.driver_ref_butom_ice_casino(StartPageConstans.url) == "my-promo7.com/ice_50fs"

#test5
def test_to_kasyna_online():
    assert start_page.driver_butom_to_kasyna_online(StartPageConstans.url) == "Lista Polskich Kasyn Online"

#test6
def test_butom_table_to_page_GG_Bet():
    assert start_page.driver_butom_to_page_GG_Bet(StartPageConstans.url) == "Polski Sloty"

#test7
def test_search_butom_main_page():
    assert start_page.driver_butom_to_kasyna_online(StartPageConstans.url) == "Book of Ra 10"
