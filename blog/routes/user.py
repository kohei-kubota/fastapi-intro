from fastapi import APIRouter, Depends
from ..schemas import User, ShowUser
from ..database import get_db
from sqlalchemy.orm import Session
from ..functions import user
from .. import oauth2

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/')
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(oauth2.get_current_user)):
    return current_user