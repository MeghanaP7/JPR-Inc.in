from fastapi import FastAPI, HTTPException, status
import sqlalchemy
from databases import Database
from pydantic import BaseModel
from typing import Optional

DATABASE_URL = "sqlite:///person_info.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)

def get_database() -> Database:
    return database

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    city: str
    country: str
    marks: int

class PersonPartialUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    marks: Optional[str] = None

class Department(BaseModel):
    id: int
    departmentName: str
    hod: str

class DepartmentPartialUpdate(BaseModel):
    id: int
    hod: Optional[str] = None

@app.on_event("startup")
async def startup():
    await get_database().connect()


@app.on_event("shutdown")
async def shutdown():
    await get_database().disconnect()


person_metadata = sqlalchemy.MetaData()
person = sqlalchemy.Table(
"person",
    person_metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("city", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("country", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("marks", sqlalchemy.Integer, nullable=True)
)

person_metadata.create_all(sqlalchemy_engine)


department_metadata = sqlalchemy.MetaData()
department = sqlalchemy.Table(
"department",
    department_metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("departmentName", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("hod", sqlalchemy.String(length=250), nullable=True)
    )

department_metadata.create_all(sqlalchemy_engine)


@app.post("/person", status_code=status.HTTP_201_CREATED)
async def create(user: Person):
    try:
        db = get_database()
        insert_query = person.insert().values(
                                                id=user.id,
                                                name=user.name,
                                                city=user.city,
                                                country=user.country,
                                                marks=user.marks,
                                                )
        await db.execute(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@app.get("/person")
async def retrieve_person():
    db = get_database()
    select_query = person.select()
    result = await db.fetch_all(select_query)
    return result


@app.get("/person/{id}", status_code=status.HTTP_200_OK)
async def get_person(id: int):
    try:
        db = get_database()
        select_query = person.select().where(person.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@app.delete("/person/{id}", status_code=status.HTTP_200_OK)
async def delete_person(id: int):
    try:
        db = get_database()
        delete_query = (person.delete().where(person.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@app.put("/person/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_person(id: int, user: Person):
    try:
        db=get_database()
        update_query = (person.update().where(person.c.id == id).values(
                                                                    id= user.id,
                                                                    name=user.name,
                                                                    city=user.city,
                                                                    country=user.country,
                                                                    marks=user.marks,
                                                                    ))
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@app.patch("/person/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_person(id: int, user: PersonPartialUpdate):
    try:
        db = get_database()
        update_query =(person.update().where(person.c.id == id).values(
                                                                        id= user.id,
                                                                        name=user.name,
                                                                        marks=user.marks,
                                                                        ))                                                                     
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    


 
@app.post("/department", status_code=status.HTTP_201_CREATED)
async def create(user: Department):
    try:
        db = get_database()
        insert_query = department.insert().values(
                                                id=user.id,
                                                departmentName=user.departmentName,
                                                hod=user.hod
                                             )
        await db.execute(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@app.get("/department")
async def retrieve_department():
    db = get_database()
    select_query = department.select()
    result = await db.fetch_all(select_query)
    return result


@app.get("/department/{id}", status_code=status.HTTP_200_OK)
async def get_department(id: int):
    try:
        db = get_database()
        select_query = department.select().where(department.c.id == id)
        result = await db.fetch_one(select_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')
    
@app.delete("/department/{id}", status_code=status.HTTP_200_OK)
async def delete_department(id: int):
    try:
        db = get_database()
        delete_query = (department.delete().where(department.c.id == id))
        result = await db.fetch_all(delete_query)
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='successfully deleted')

@app.put("/department/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_department(id: int, user: Department):
    try:
        db=get_database()
        update_query = (department.update().where(person.c.id == id).values(
                                                                            id= user.id,
                                                                            departmentName=user.departmentName,
                                                                            hod=user.hod
                                                                            ))                               
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')

@app.patch("/department/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_person(id: int, user: DepartmentPartialUpdate):
    try:
        db = get_database()
        update_query =(person.update().where(person.c.id == id).values(
                                                                        id= user.id,
                                                                        hod=user.hod,
                                                                        ))                                                                 
        result = await db.fetch_one(update_query)
        if result is None:
            return None
        return result
    except Exception as e:
        print(e.args[0])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')    
