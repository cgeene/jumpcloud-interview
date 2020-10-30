import requests
from flask import current_app


def generic_request(request, method, path, kwargs):
    response = requests.request(
        method,
        current_app.config["JUMPCLOUD_BASE_URL"] + path,
        headers=request.headers,
        **kwargs
    )
    return response.json()


def get_users(request):
    kwargs = {"params": request.args}
    return generic_request(request, "GET", "/systemusers", kwargs)


def create_user(request):
    kwargs = {"json": request.json}
    return generic_request(request, "POST", "/systemusers", kwargs)


def get_user_by_id(request, id):
    return generic_request(request, "GET", "/systemusers/" + id, {})


def update_user(request, id):
    kwargs = {"json": request.json}
    return generic_request(request, "PUT", "/systemusers/" + id, kwargs)


def delete_user(request, id):
    return generic_request(request, "DELETE", "/systemusers/" + id, {})


def get_user_count(request):
    kwargs = {"params": {"limit": 1}}
    response = generic_request(request, "GET", "/systemusers", kwargs)
    return {"totalCount": response["totalCount"]}
