import requests

def getCredencials():

    res = requests.get('https://script.google.com/macros/s/AKfycbw_gBk0qxq2yIo5uTqCwARPg8HcYmjMFWZcXx1dAEVJMa5lnNszwK3ys9PRK3YqJ436/exec')
    
    if res.status_code != 200:
        print(f'route error: {res.status_code}')
    else:
        request_json = res.json()
        
        return  request_json
