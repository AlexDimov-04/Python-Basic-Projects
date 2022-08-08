# importing modules
import urllib.request
import requests
from PIL import Image

# api key/request url
api_url = "https://dog.ceo/api/breeds/image/random"

# requests data from url
data = requests.get(api_url)
data = data.json()

# finds the image url and name it with a proper filename
urllib.request.urlretrieve(data['message'], 'random_dog_pic')

# opens the image
img = Image.open("random_dog_pic")
img.show()
