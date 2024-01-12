import requests

url = "https://file-examples.com/storage/fe9d743740654a8139a48e1/2017/02/zip_10MB.zip"

webpage = requests.get(url)

futureName = url.split('/')[-1]

with open(futureName, 'wb') as file:
    file.write(webpage.content)
