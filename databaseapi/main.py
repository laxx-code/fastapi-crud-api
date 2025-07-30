from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from typing import List

app = FastAPI()

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db'  # Correct format for SQLite

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database model
class Todo(Base):
    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    todoname = Column(String, index=True)
    tododescription = Column(String, index=True)
    assigneduser = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class TodoResponse(BaseModel):
    id: int
    todoname: str
    tododescription: str
    assigneduser: str

    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    taskname: str
    taskdescription: str
    assigneduser: str

# Route to create a task
@app.post('/createtask/', response_model=TodoResponse)
def create_task(task: TodoCreate, db: Session = Depends(get_db)):
    newtask = Todo(
        todoname=task.taskname,
        tododescription=task.taskdescription,
        assigneduser=task.assigneduser
    )
    db.add(newtask)
    db.commit()
    db.refresh(newtask)
    return newtask


# ahow all with id
@app.get('/todos/', response_model=List[TodoResponse])
def display_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todolist = db.query(Todo).offset(skip).limit(limit).all()
    return todolist

# get by id
@app.get('/todos/{todo_id}', response_model=TodoResponse)
def get_user(todo_id: int, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == todo_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return task

@app.get('/')
def testing():
    return'working'