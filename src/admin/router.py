from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
import src.database as db
from src.auth import schemas,services
from src.tasks import services as taskServices
from src.admin import services as adminServices
from src.tasks import schemas as taskSchemas 
from src.auth.jwt import get_current_user
from src.auth.models import User

router = APIRouter(tags=['Admin'], prefix='/admin')


@router.get('/users', response_model=List[schemas.DisplayAccount])
async def get_all_users(database: Session = Depends(db.get_db), current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await services.all_users(database)


@router.get('/users/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.DisplayAccount)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await adminServices.get_user_by_id(user_id, database)


@router.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int,
                                database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await adminServices.delete_user_by_id(user_id, database)


@router.patch('/users/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.DisplayAccount)
async def update_user_by_id(request: schemas.UserUpdate, user_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):

    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")                            
    return await adminServices.update_user_by_id(request, user_id, database)


@router.get('/tasks', status_code=status.HTTP_200_OK, response_model=List[taskSchemas.TaskBase])
async def get_user_by_id(database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await adminServices.all_tasks(database)


@router.delete('/tasks/delete', status_code=status.HTTP_200_OK)
async def delete_all_tasks(database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await adminServices.delete_all_tasks(database)


@router.get('/tasks/{task_id}', status_code=status.HTTP_200_OK, response_model=taskSchemas.TaskBase)
async def get_task_by_id(task_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await taskServices.get_task_by_id(task_id, database)


@router.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_task_by_id(task_id: int,
                                database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")
    return await adminServices.delete_task_by_id(task_id, database)


@router.patch('/tasks/{task_id}', status_code=status.HTTP_200_OK, response_model=taskSchemas.TaskBase)
async def update_user_by_id(request: taskSchemas.TaskUpdate, task_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):

    user = database.query(User).filter(User.email == current_user.email).first()
    if user.role != 'admin':
        raise HTTPException(status_code=403, detail="Only admins are allowed to perform this action")                            
    return await adminServices.update_task_by_id(request, task_id, database)