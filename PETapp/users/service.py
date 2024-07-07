from PETapp.services.base import BaseService
from PETapp.users.models import Users


class UserService(BaseService):
    model = Users
