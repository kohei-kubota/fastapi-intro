from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..schemas import Blog, ShowBlog, User
from ..database import get_db
from .. import models, oauth2
from sqlalchemy.orm import Session
from ..functions import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)

@router.get('/', response_model=List[ShowBlog])
async def all_fetch(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    user_id = [d for d in current_user]
    print(user_id[0].id)
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id:int, response: Response,  db: Session = Depends(get_db)):
    return blog.show(id, db)