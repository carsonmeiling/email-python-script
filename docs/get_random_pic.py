import requests, json, random

def get_image():
  with open('key.json', 'r') as f:
    json_object = json.loads(f.read())

  base_url = 'https://pixabay.com/api/'
  # api_key = json_object('api_key')
  api_key = '24300858-ce1d79139e516c673da1f4014'
  q = 'puppies'
  random_number = random.randint(0,11)

  complete_url = base_url + '?key=' + api_key + '&q=' + q + '&image_type=image' 
  # print(complete_url)

  response = requests.get(complete_url)
  x = response.json()

  # print(random_number)
  image_jpg = x['hits'][random_number]['largeImageURL']
  page_url = x['hits'][random_number]['pageURL']
  
  total_response = x['total']
  # print(total_response)
  # print(type(image_jpg))
  # print(type(page_url))
  return page_url

get_image()