from fastapi import Depends, HTTPException
from fastapi.security import APIKeyCookie, HTTPBearer, HTTPAuthorizationCredentials

from . import services

bearer_scheme = HTTPBearer(scheme_name="access_token", auto_error=False)
refresh_cookie = APIKeyCookie(name="refresh", scheme_name="refresh_cookie", auto_error=False)

def get_current_user(
    bearer: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    if not bearer:
        raise HTTPException(status_code=401, detail="Missing access token")

    token = bearer.credentials
    user_id = services.decode_token(token)

    return user_id