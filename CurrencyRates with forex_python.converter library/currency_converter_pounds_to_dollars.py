# import module
from forex_python.converter import CurrencyRates

# amount of money
amount = int(input("Enter the number of pounds: "))
# initialize the currency_rate
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
# sum and print the result
result = current_rate * amount
print(f'Your sum in dollars is {result:.2f}')
