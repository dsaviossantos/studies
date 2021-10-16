from flask.globals import request
import  requests

BASE = "http://127.0.0.1:5000"

data = [{"likes": 2987, "name": "Video's Name 1", "views": 92289},
        {"likes": 1019, "name": "Video's Name 2", "views": 81192},
        {"likes": 1987, "name": "Video's Name 3", "views": 9887}]

for i in range(len(data)):
    response = requests.put(BASE + "/video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "/video/0")
print(response)
input()
response = requests.get(BASE + "/video/0")
print(response.json())