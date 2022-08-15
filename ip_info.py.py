import requests
import json

ip = input("Enter IP to Lookup: ")

url = f"https://ipapi.co/{ip.strip()}/json/"

contents = requests.get(url)
print("------ RAW Output ------")
print(contents)
print("------ FORMATTED Output ------")
print(json.dumps(contents.json(), indent=4))



# git log --pretty=format:"%h - %an, %ar : %s"