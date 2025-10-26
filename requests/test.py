import requests

res = requests.get("https://api.github.com")


ret = res.headers["Content-Type"]
print(ret)