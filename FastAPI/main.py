from fastapi import FastAPI
from pydantic import BaseModel
# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return { "message": "Hello, FastAPI!"}

@app.get('/about')
def about():
    return {'data':"ihi this is rhergh",'dire':{'data':"ehuiugoj po rhugo"}}

# path parameter
@app.get('/user/{id}')
def displayuser(id):
    return f'user with id={id} is displayed'
#it retrun type of data
    # return id
# to convert in another datatype or to assign
    #return f'user with id={id} is displayed'

# query parameter
@app.get('/user')
def conditionuser(limit:int,failed:bool=True,sort:str| None=None):
    if failed== True:
        return f'failed {limit} users list'
    else:
        return 'all student'
    
#POST METHOD
class CreateModel(BaseModel):
    name:str
    age:int|None=None
    email:str
    phone:int
@app.post ('/adduser')
def createuser(request:CreateModel):
    return request





























    #swagger ui 