from core.services.user_services import UserService
from core.models import User
from core.exceptions.base_error import BaseError
from werkzeug.security import check_password_hash
from src.services.repository.user import UserRepository
from src.services.app_services import AppService

""" This files is an login implementation of User functionality.
    In view the below function will get call through services module.
    It takes UserService as abstract class which is in core/service/user_service.py
"""


class UserServiceImpl(UserService):

    def __init__(self, user_repository: UserRepository, services: AppService, config):
        self.user_repository = user_repository
        self.services = services
        self.config = config

    def add_user(self, user: User) -> BaseError:
        user_duplicate = self.user_repository.get_user_by_email(user.email)

        user_error = BaseError()

        if user_duplicate is not None:
            user_error.has_error = True
            user_error.global_error['has_error'] = True
            user_error.global_error['message'] = "Email Id Already Used. Please Use Different Email Id"
        else:
            uid = self.user_repository.add_user(user)
            user_error.global_error['message'] = user.firstname + ' user registered'
            user_error.global_error['data'] = uid.email
        return user_error

    def user_login(self, user: User) -> BaseError:
        user_detail = self.user_repository.get_user_by_email(user.email)

        user_error = BaseError()
        if user_detail is None:
            user_error.has_error = True
            user_error.global_error['has_error'] = True
            user_error.global_error['message'] = "This email id is not available"
            return user_error
        elif not check_password_hash(user_detail.password, user.password):
            user_error.has_error = True
            user_error.global_error['has_error'] = True
            user_error.global_error['message'] = "Invalid Password"
            return user_error
        elif check_password_hash(user_detail.password, user.password):
            # user_error.user_obj = user_detail
            user_error.global_error['data'] = user_detail.email
            user_error.global_error['message'] = "User has logged In"
            return user_error
