import requests

res = requests.get("https://script.google.com/macros/s/AKfycbw_gBk0qxq2yIo5uTqCwARPg8HcYmjMFWZcXx1dAEVJMa5lnNszwK3ys9PRK3YqJ436/exec")

resjson = res.json()

print(resjson["email"])