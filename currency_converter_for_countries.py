# import modules
from forex_python.converter import CurrencyRates
import datetime as dt

# currency rates for a specific data
date = dt.datetime(2022, 1, 21)
# define the CurrencyRates
c = CurrencyRates()
# list with a specific countries with currency rate
countries = ['GBP', 'EUR', 'BGN', 'INR', 'SEK', 'CHF']

# pick a specific country currency rate at a specific datetime
print(f"BGN Currency rates as of {date}")
for i in countries:
    print(c.get_rate('BGN', i, date), i)
