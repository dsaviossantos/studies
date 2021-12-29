import  requests
import json
import time

BASE = "http://localhost:5000"

tic = time.perf_counter()
i = 0
while i < 100:
    data = {
        "email": "email@email.com"+str(i),
        "name": "Joe Doe",
        "location": {
                "address": "Rua do Webhook, 123",
                "district":"Webhood",
                "city":"Webcity",
                "state":"Webstate",
                "country":"Webcountry",
                "zipcode":"12365487"
                },
            "gender":"Webgender"}

    i += 1
    time.sleep(1)
    response = requests.post(BASE + "/user",json=data)

toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")