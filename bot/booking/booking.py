import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        super().__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            self.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        except:
            print('Didnt find the element')

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Vybrať menu"]'
        )
        currency_element.click()
        selector = f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, selector
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)