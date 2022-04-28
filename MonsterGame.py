from urllib import response
import requests

response1 = requests.get("https://random-word-api.herokuapp.com/word").json()[0]
response2 = requests.get("https://random-word-api.herokuapp.com/word").json()[0]
name = response1 + "-" + response2


print(name)