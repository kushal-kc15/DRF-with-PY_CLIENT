import requests

# endpoint="https://httpbin.org/status/200"
endpoint="https://httpbin.org/anything"

get_response=requests.get(endpoint,json={"query":"python"}) #HTTP Request
# print(get_response.text) #print raw tect response

#HTTP Request -> Html
#REST API HTTP Request -> JSON

#JavaScript Object Notation ~ Python Dict
# print(get_response.json())
print(get_response.status_code)
