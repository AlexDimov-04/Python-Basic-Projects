# import modules
from datetime import datetime, timedelta
import locale

# setlocale to bulgarian latitude
locale.setlocale(locale.LC_ALL, "bulgarian")
# extract the current time
z = datetime.now()
# format the date
formatted_z = datetime.strftime(z, '%A %B %d %Y')
# print the date
print(formatted_z)
