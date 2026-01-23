import requests

headers={"Authorization":"Bearer a21e1bb378c76bc8168fd9152d27f2f930bf43ca"}
endpoint="http://localhost:8000/api/products/"
data={
    "title":"hello world",
    "price":12.99
}
get_response=requests.post(endpoint,data=data,headers=headers)
print(get_response.json())
