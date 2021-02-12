import requests
import datetime
import os

pixela_endpoint = "https://pixe.la/v1"
graph = "habit-graph"
token = os.environ.get("TOKEN")
username = "densemode"
today = datetime.datetime.now()

# payload= {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# # res = requests.post(url=pixela_endpoint, json=payload)
# print(res.text)

# url = f"{pixela_endpoint}/users/{username}/graphs"
# print(url)
# headers = {
#     "X-USER-TOKEN": token
# }
#
# payload = {
#     "id":"habit-graph",
#     "name": "densemode-habits",
#     "unit": "laughs",
#     "type": "int",
#     "color": "shibafu",
#     "timezone": "America/New_York"
# }
#
# res = requests.post(url=url, headers=headers, json=payload)
# print(res.text)

# url = f"https://pixe.la/v1/users/{username}/graphs/{graph}"
#
# headers = {
#     "X-USER-TOKEN": token
# }
#
# payload = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "50"
# }
#
# res = requests.put(url=url, headers=headers, json=payload)
# print(res.text)


url = f"https://pixe.la/v1/users/{username}/graphs/{graph}/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": token
}

payload = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

res = requests.put(url=url, headers=headers, json=payload)
print(res.text)