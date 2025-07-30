from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()
ToDolist={
    1:{
        "taskname":"wrting",
        "taskdescription":"wrte 10 page a day now",
        "assigneduser":"user1"
    },
    2:{
        "taskname":"playing,",
        "taskdescription":"football is payed",
    }
}

@app.get('/displaytask')
def displayTask():
    return ToDolist

class CreateTaskMOdel(BaseModel):
    taskid:int
    taskname:str
    taskdescription:str
    moreinfo:str |None=None

@app.post('/createTask')
def createTask(task:CreateTaskMOdel):
    if not ToDolist:
        new_id =1
        task.taskid=new_id
    else:
        new_id = max(ToDolist.keys(),default=0) + 1
        task.taskid=new_id
        ToDolist[new_id]=task.model_dump()
        return ToDolist[new_id]
    
# pydantic model for updationg

class Taskupdatemodel(BaseModel):
    taskname:Optional[str]=None
    taskdescription:Optional[str]=None
    moreinfo:Optional[str]=None
    assigneduser:Optional[str]=None

@app.put('/updatetask')
def update_task(task_id:int,task:Taskupdatemodel):
    if task_id not in ToDolist:
        return f"no task found with {task_id}"
    else:
        if task.taskname is not None:
            ToDolist[task_id] ['taskname']=task.taskname
        if task.taskdescription is not None:
            ToDolist[task_id] ['taskdescription']=task.taskdescription
        if task.moreinfo is not None:
            ToDolist[task_id]['moreinfo']=task.moreinfo
        if task.assigneduser is not None:
            ToDolist[task_id]['assgineduser']=task.assigneduser
        return ToDolist[task_id]
    
@app.delete('/deleteuser/{task_id}')
def deleteTask(task_id:int):
    if task_id not in ToDolist:
        return f"no task found with{task_id}"
    del ToDolist[task_id]
    return ToDolist