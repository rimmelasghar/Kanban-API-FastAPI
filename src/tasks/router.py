from typing import List
from fastapi import APIRouter, Depends, status, Response, Request
from sqlalchemy.orm import Session
from src.auth.jwt import get_current_user
from src.auth.models import User
import src.database as db

from . import schemas
from . import services


router = APIRouter(tags=["Task"],prefix='/task')


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.TaskBase)
async def create_new_task(request: schemas.TaskBase, database: Session = Depends(db.get_db), 
    current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.email == current_user.email).first()
    result = await services.create_new_task(request, database, user)
    return result


@router.get('/', status_code=status.HTTP_200_OK,
            response_model=List[schemas.TaskList])
async def task_list(database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    result = await services.get_task_listing(database, current_user.id)
    return result


@router.get('/{task_id}', status_code=status.HTTP_200_OK, response_model=schemas.TaskBase)
async def get_task_by_id(task_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    return await services.get_task_by_id(task_id, current_user.id, database)


@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_task_by_id(task_id: int,
                                database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    return await services.delete_task_by_id(task_id, database)


@router.patch('/{task_id}', status_code=status.HTTP_200_OK, response_model=schemas.TaskBase)
async def update_task_by_id(request: schemas.TaskUpdate, task_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    return await services.update_task_by_id(request, task_id, current_user.id, database)