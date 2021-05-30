from src import app, services, login_manager
from core.models import User
from core.exceptions.base_error import BaseError
from flask_login import login_user, logout_user, login_required, current_user
from flask import request, session
from werkzeug.security import generate_password_hash

from src.services.repository.user import UserRepository

''' This files performs operation related to users
    The User is database model, services will use to call function of src/services/impl/ file which has actual login implementation.
'''
@login_manager.user_loader
def load_user(user_id):
    user_service = UserRepository()
    user = user_service.get_user_by_email(email=user_id)
    return user


@app.route(app.config['SIGNUP_URL'], methods=['POST'])
def user_registration():
    try:
        user = User()
        data = request.get_json()

        user.firstname = data['firstname']
        user.lastname = data['lastname']
        user.email = data['email']
        password = data['password']
        user.password = generate_password_hash(password)

        user_service = services.get_user_service()
        error_obj = user_service.add_user(user=user)
        # db.session.add(user)
        if error_obj.has_error:
            return error_obj.global_error
        else:
            return error_obj.global_error
    except Exception as e:
        print(e)
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"


@app.route(app.config['LOGIN_URL'], methods=['POST'])
def user_login():
    try:
        data = request.get_json()
        user = User()
        user.email = data['email']
        user.password = data['password']
        user_service = services.get_user_service()

        error_obj = user_service.user_login(user=user)
        if error_obj.has_error:
            return error_obj.global_error
        else:
            user_service = UserRepository()
            user = user_service.get_user_by_email(email=data['email'])
            login_user(user, remember=True)
            return error_obj.global_error
    except Exception as e:
        print(e)
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"


@app.route(app.config['LOGOUT_URL'], methods=["GET"])
@login_required
def user_logout():
    try:
        user = current_user
        user_email = user.get_id()
        user.authenticated = False
        logout_user()
        error_obj = BaseError()
        error_obj.global_error['data'] = user_email
        error_obj.global_error['message'] = "User has logged out"

    except Exception as e:
        print(e)
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"

    return error_obj.global_error
