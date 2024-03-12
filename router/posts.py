from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models as models
import Schema as schemas 
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/states',
    tags=['state']
)

@router.get('/', response_model=list[schemas.CreatePost])
async def getAllStates(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()

    return post

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost])
async def postAllStates(posts: List[schemas.CreatePost], db: Session = Depends(get_db)):
    new_posts = []
    for post in posts:
        new_post = models.Post(**post.dict())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        new_posts.append(new_post)
    return new_posts

@router.get('/{abbreviation}', response_model=schemas.CreatePost, status_code=status.HTTP_200_OK)
async def getState(abbreviation: str, db: Session = Depends(get_db)):
    idv_post = db.query(models.Post).filter(models.Post.abbreviation == abbreviation).first()
    if idv_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The abbreviation: {abbreviation} you requested for does not exist")
    return idv_post

@router.delete('/{abbreviation}', response_model=schemas.CreatePost, status_code=status.HTTP_200_OK)
async def delete_test_post(abbreviation: str, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.abbreviation == abbreviation).first()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The abbreviation: {abbreviation} you requested for does not exist")
    db.delete(deleted_post)
    db.commit()
    return deleted_post

@router.put('/', response_model=schemas.CreatePost)
async def update_test_post(update_post: schemas.PostBase, db: Session = Depends(get_db)):
    abbreviation = update_post.abbreviation
    existing_post = db.query(models.Post).filter(models.Post.abbreviation == abbreviation).first()
    
    if existing_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The abbreviation: {abbreviation} does not exist")
    
    # Update the existing post's attributes
    existing_post.state = update_post.state
    
    db.commit()
    # Return the updated post
    return existing_post