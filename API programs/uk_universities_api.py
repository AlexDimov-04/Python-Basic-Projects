# importing modules
import requests
import random

# api key/request url
key = "http://universities.hipolabs.com/search?country=United+Kingdom"

# requests data from url
data = requests.get(key)
data = data.json()

# pick a random university
random_university = data[random.randrange(0, 347)]

# print university data
print(f"University name: {random_university['name']}")
print(f"Country: {random_university['country']}")
print(f"University web page: {''.join(random_university['web_pages'])}\n")
print(f"State-province: {random_university['state-province']}")
print(f"Alpha_two_code: {random_university['alpha_two_code']}")
print(f"Domains: {', '.join(random_university['domains'])}")
