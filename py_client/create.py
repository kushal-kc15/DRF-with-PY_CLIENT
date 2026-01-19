import requests
endpoint="http://localhost:8000/api/products/create/"
data={
    "title":"hello world",
    "content":"Hello World",
    "price":12.99
}
get_response=requests.post(endpoint,data=data)
print(get_response.json())