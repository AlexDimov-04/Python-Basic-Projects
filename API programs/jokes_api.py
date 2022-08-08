# importing modules
import requests
from time import sleep

# api key/request url
key = "https://v2.jokeapi.dev/joke/Any?safe-mode"

# requests data from url
data = requests.get(key)
data = data.json()

# managing if statements for a static jokes and jokes with a punchline
if 'joke' in data:
    print(data['joke'])
else:
    print(data['setup'])
    for dot in range(5):
        sleep(1)
        print('*')
    print(data['delivery'])
