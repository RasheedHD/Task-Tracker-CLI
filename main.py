from json import loads, dumps, load, dump

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def updateStatus(self, newStatus):
        self.status = newStatus
    

def convert_to_json(task):
    dic = {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": task.createdAt,
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

tasks = [Task(1,2,3,4,5), Task(4,3,5,4,1), Task(1,1,3,4,1), Task(3,3,3,4,5)]
saveTasks(tasks)