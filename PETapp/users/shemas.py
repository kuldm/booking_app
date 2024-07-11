from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str

    class Config:
        from_attributes = True
