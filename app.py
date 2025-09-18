# API klici(spletni klici)

import requests
import json

#baseURL = "https://www.google.com/"
#call = requests.get(baseURL)#metoda routea get

#print (call.text)#text pridobi raw data call

#scrape.

#API klici/calli - ne vrača HTML - vrača JSON, XML
"""
baseURL= "https://api.chucknorris.io/jokes/random"

klic = requests.get(baseURL)

#print (klic)
#ugotovimo, če os podatki JSON
#print(klic.text)
#ko smo 100% da so podatki JSON
js=klic.json()
print(js.get("value"))"""

"""baseurl="https://api.nationalize.io/?name="
ime=input("Vnesi ime: ")

klic = requests.get(baseurl + ime).json()
#print(klic.url)#preverimo generiran URL
print(klic.get("count"))
print(klic.get("name"))

drzave= klic.get("country")

for d in drzave:
    print(d.get("country_id"), d.get("probability")*100)"""

baseurl="https://sv443.net/jokeapi/v2/joke/Any"
call = requests.get(baseurl)
call=call.json()
#print(json.dumps(call, indent=4)) !!!!Izpiše vse value v JSON obliki

print(call.get("setup"))
print(call.get("delivery"))