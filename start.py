from lib.Currency import Currency
from lib.Covid19 import Covid19
import time

currency = Currency()
covid19 = Covid19()

counter = 0
while True:
    counter+=1
    print("Get online data => ", counter, " times")
    currency.start()
    covid19.start()
    time.sleep(300)