from flask import Blueprint, request
from flaskr.db import (
    create_user as db_create_user,
    update_user as db_update_user,
    delete_user as db_delete_user,
)
from flaskr.jumpcloud import (
    get_users,
    create_user,
    get_user_by_id,
    get_user_count,
    update_user,
    delete_user,
)

bp = Blueprint("users", __name__)


@bp.route("/users", methods=["GET", "POST"])
def create_or_search():
    if request.method == "GET":
        return get_users(request)
    else:
        response = create_user(request)
        db_create_user(response)
        return response


@bp.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def detail(user_id):
    if request.method == "GET":
        return get_user_by_id(request, user_id)
    elif request.method == "PUT":
        response = update_user(request, user_id)
        db_update_user(response)
        return response
    else:
        response = delete_user(request, user_id)
        db_delete_user(response)
        return response


@bp.route("/users/count", methods=["GET"])
def user_count():
    return get_user_count(request)
