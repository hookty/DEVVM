# key : 51p6q5iZxGw6GVdcCjvEGvYowFgGGABd

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italia"
dest = "Frascati, Italia"
key = "51p6q5iZxGw6GVdcCjvEGvYowFgGGABd"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)

