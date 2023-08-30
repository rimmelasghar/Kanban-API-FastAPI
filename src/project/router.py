from typing import List
from fastapi import APIRouter, Depends, status, Response, Request
from sqlalchemy.orm import Session
from src.auth.jwt import get_current_user
from src.auth.models import User
import src.database as db
from . import schemas
from . import services


router = APIRouter(tags=["Project"],prefix='/project')


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=schemas.ProjectBase)
async def create_new_project(request: schemas.ProjectBase, database: Session = Depends(db.get_db), 
    current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.email == current_user.email).first()
    result = await services.create_new_project(request, database, user)
    return result


@router.get('/', status_code=status.HTTP_200_OK,
            response_model=List[schemas.ProjectList])
async def project_list(database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    result = await services.get_project_listing(database, current_user.id)
    return result


@router.get('/{project_id}', status_code=status.HTTP_200_OK, response_model=schemas.ProjectBase)
async def get_project_by_id(project_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    return await services.get_project_by_id(project_id, current_user.id, database)


@router.delete('/{project_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_project_by_id(project_id: int,
                                database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):
    return await services.delete_project_by_id(project_id, database)


@router.patch('/{project_id}', status_code=status.HTTP_200_OK, response_model=schemas.ProjectBase)
async def update_project_by_id(request: schemas.ProjectUpdate, project_id: int, database: Session = Depends(db.get_db),
                                current_user: User = Depends(get_current_user)):                            
    return await services.update_project_by_id(request, project_id, current_user.id, database)