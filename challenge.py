#Test json get on a URL
import urllib.request, json

with urllib.request.urlopen("https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios") as url:
    data = json.load(url)
    print(data)
