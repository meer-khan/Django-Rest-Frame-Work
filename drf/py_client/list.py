import requests 

endpoint= "http://localhost:8080/api/products/"
# data = {
#     "title":"this field is done",
#     "price" :32.99
# }

getResponse = requests.get(endpoint)
print(getResponse.json())