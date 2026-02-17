from json import loads, dumps, dump
from datetime import datetime

class Task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = "N/A"

    def updateDescription(self, description):
        self.status = description
        self.updatedAt = datetime.now()

    def updateStatus(self, status):
        self.status = status
        self.updatedAt = datetime.now()
    

def convert_to_json(task):
    dic = {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": str(task.createdAt),
        "updatedAt": task.updatedAt
    }
    return dumps(dic)

def convert_to_dic(task):
    return loads(task)

def saveTasks(tasks):
    tasksD = list(map(convert_to_json, tasks))
    with open("tasks.json", "w") as tasksFile:
        dump(tasksD, tasksFile, indent=4)

def addTask(task):
    tasks.append(task)

def deleteTask(task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            break

tasks = [Task(1,2,3), Task(4,3,5), Task(1,1,3), Task(5,3,9)]
saveTasks(tasks)