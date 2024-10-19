import requests

url = "POST|/api/v1/users/:user_id/tokens"

token = requests.post(url)
