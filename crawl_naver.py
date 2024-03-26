import requests

r = requests.get("https://naver.com")
with open("naver.txt", "w", encoding='utf-8') as f:
    f.write(r.text)