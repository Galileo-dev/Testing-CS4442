import traceback
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status, Response, FastAPI, Depends
from firebase_admin import auth
from fastapi import APIRouter
import os

router = APIRouter()





# signup endpoint (not implemented)

# login endpoint
async def get_user_token(res: Response, credential: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
    if credential is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication is needed",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
        print(credential.credentials)
        
        decoded_token = auth.verify_id_token(credential.credentials)
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication from Firebase. {err}",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
        )
    res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
    return decoded_token


@router.get("/api/")
async def hello():
    return {"msg": "Hello, this is API server"}


@router.get("/api/user_token")
async def hello_user(user=Depends(get_user_token)):
    return {"msg": "Hello, user", "uid": user['uid']}
