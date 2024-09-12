from pydantic import BaseModel

class DateFilterRequest(BaseModel):
    start_date: str
    end_date: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str