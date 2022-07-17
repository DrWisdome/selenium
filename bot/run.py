from select import select
from time import sleep
from booking.booking import Booking


with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency(currency='GBP')
    bot.select_place_to_go('New York')
    bot.select_date(check_in='2022-07-18',check_out='2022-07-22')
    bot.select_num_adults(5)
    bot.submit()

