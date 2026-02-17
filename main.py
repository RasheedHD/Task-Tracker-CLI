from json import loads, dumps, dump
from datetime import datetime

class Task:
    def __init__(self, id, description, status="todo"):
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

    def getDateString(self, type):
        if type == "c":
            return str(self.createdAt)[:-10]
        elif type == "u":
            return str(self.updatedAt)[:-10] if self.updatedAt != "N/A" else "N/A"
    

def convert_to_json(task):
    dic = {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": task.getDateString("c"),
        "updatedAt": task.getDateString("u")
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

def listTasks(s):
    tasksToView = []
    if s == "all":
        tasksToView = tasks
    elif s in ["done", "todo", "in-progress"]:
        for task in tasks:
            if task.status == s:
                tasksToView.append(task)
    else:
        pass # TODO: throw error

    print("="*96)
    print(f"{"ID":<5} {"Description":<30} {"Status":<8} {"Created At":<20} {"Updated At":<20}")
    for task in tasksToView:
        print(f"{task.id:<5} {task.description:<30} {task.status:<8} {task.getDateString("c"):<20} {task.getDateString("u"):<20}")


tasks = [Task(1,"Walk the cat", "done"), Task(2,"Build a project", "done"), Task(3,"Study at home"), Task(4,"Clean the dishes")]


listTasks("todo")




#saveTasks(tasks)