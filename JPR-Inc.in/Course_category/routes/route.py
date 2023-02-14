from fastapi import APIRouter
from db import get_database
from fastapi import status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from models.model import course_category

router = APIRouter()

class CourseCategory(BaseModel):
    id: int
    name: str
    description: str
    created_date: datetime
    updated_date: datetime

class CourseCategoryPartialUpdate(BaseModel):
    id: int
    description: str


@router.post("/course_category", status_code=status.HTTP_201_CREATED)
async def data(user: CourseCategory):
    try:
        db = get_database()
        insert_query = course_category.insert().values(id=user.id,
                                                       name=user.name,
                                                       description=user.description,
                                                       created_date=user.created_date,
                                                       updated_date=user.updated_date
                                                       )
        await db.execute(insert_query)
        # print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_category")
async def retrieve_course_category():
    db = get_database()
    select_query = course_category.select()
    result = await db.fetch_all(select_query)
    return result


@router.get("/course_category/{id}")
async def get_course_category(id: int):
    try:
        db = get_database()
        select_query = course_category.select().where(course_category.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])

@router.delete("/course_category/{id}", status_code=status.HTTP_200_OK)
async def delete_course_category(id: int):
    try:
        db = get_database()
        delete_query = (course_category.delete().where(course_category.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@router.put("/course_category/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_category(id: int, user: CourseCategory):
    try:
        db=get_database()
        update_query = (course_category.update().where(course_category.c.id == id).values(id=user.id,
                                                                                          name=user.name,
                                                                                          description=user.description,
                                                                                          created_date=user.created_date,
                                                                                          updated_date=user.updated_date
                                                                                          ))              
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@router.patch("/course_category/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_course_category(id: int, user: CourseCategoryPartialUpdate):
    try:
        db = get_database()
        update_query =(course_category.update().where(course_category.c.id == id).values(
                                                                                         id= user.id,
                                                                                         description=user.description
                                                                                         ))                                                                 
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    
