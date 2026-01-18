import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={"product_id": 123})

print("Status Code:", get_response.status_code)
print("Content-Type:", get_response.headers.get('Content-Type'))
print("Response Text:")
print(get_response.text)
print("\n" + "="*50)

# Only try to parse JSON if status is 200 and content-type is JSON
if get_response.status_code == 200:
    try:
        print("JSON Response:")
        print(get_response.json())
    except Exception as e:
        print(f"Error parsing JSON: {e}")
else:
    print(f"Error: Server returned status code {get_response.status_code}")
