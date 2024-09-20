import requests
api_url="http://127.0.0.1:8000/create_person"

person_data={
    "name":"Alma",
    "age":27
}
response = requests.post(api_url, json=person_data)
print(response.status_code)
print(response.json())