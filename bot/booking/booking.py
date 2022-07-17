import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        super().__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
