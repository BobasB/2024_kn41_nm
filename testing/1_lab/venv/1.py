import requests

print("Це запустилось у Віртуальному середовищі")
r = requests.get('https://google.com')
print(f"Відповідь сервера: {r.status_code}")
