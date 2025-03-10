from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from PETapp.config import settings
from PETapp.users.service import UserService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserService.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user

# Generate secret key
# from secrets import token_bytes
# from base64 import b64encode
# print(b64encode(token_bytes(32)).decode())
