import requests

# endpoint="https://httpbin.org/status/200"
# endpoint="https://httpbin.org/anything"
endpoint="http://localhost:8000/api"

get_response=requests.get(endpoint,params={"product_id ":123}) #HTTP Request
# print(get_response.text) #print raw tect response
print(get_response.json())
# print(get_response.status_code)

#HTTP Request -> Html
#REST API HTTP Request -> JSON

#JavaScript Object Notation ~ Python Dict
# print(get_response.json())
