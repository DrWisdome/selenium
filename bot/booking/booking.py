from audioop import add
from tkinter import N
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        super().__init__()
        self.implicitly_wait(20)
        #self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        try:
            element = self.find_element(By.ID, 'onetrust-accept-btn-handler')
            element.click()
        except:
            print('Didnt find the element')

    def change_currency(self, currency='EUR'):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Vybrať menu"]'
        )
        currency_element.click()

        selector = f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        selected_currency_element = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR,'li[data-i="0"]')
        first_result.click()

    def select_date(self, check_in, check_out):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        check_out_element.click()
    def select_num_adults(self, num_adults):
        num_adults_element = self.find_element(By.ID, 'xp__guests__toggle')
        num_adults_element.click()
        act_num_adults = self.find_element(By.CSS_SELECTOR, 'span[data-bui-ref="input-stepper-value"]')
        add_one = self.find_element(By.CSS_SELECTOR, 'button[data-bui-ref="input-stepper-add-button"]')
        while(int(act_num_adults.text)<num_adults):
            add_one.click()    

    def submit(self):
        submit_button = self.find_element(By.CSS_SELECTOR, 'button[data-sb-id="main"]')
        submit_button.click()