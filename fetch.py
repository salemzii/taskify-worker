import requests



base_url = "https://bit-taskify.herokuapp.com/"
local_url = "http://localhost:8000/"

def get_UserById(id: int) -> dict | None:
    endpoint = local_url + f"api/users/{id}"
    req = requests.get(endpoint)
    body = None
    if req.status_code == 200:
        body = req.json()
        return body
    return body
