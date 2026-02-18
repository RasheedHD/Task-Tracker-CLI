from json import loads, dumps, dump
from datetime import datetime

class Task:
    num = 0
    def __init__(self, description, status="todo"):
        Task.num += 1
        self.id = Task.num
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

def saveTasks():
    tasksD = list(map(convert_to_json, tasks))
    with open("tasks.json", "w") as tasksFile:
        dump(tasksD, tasksFile, indent=4)

def addTask(task):
    tasks.append(task)

def deleteTask(task_id):
    tasks.remove(findTask(task_id))

def listTasks(s):
    tasksToView = []
    if s == "all":
        tasksToView = tasks
    elif s in ["done", "todo", "in-progress"]:
        for task in tasks:
            if task.status == s:
                tasksToView.append(task)
    else:
        raise Exception
    if not tasksToView:
        print("No tasks yet")
        return
    print("="*96)
    print(f"{"ID":<5} {"Description":<30} {"Status":<8} {"Created At":<20} {"Updated At":<20}")
    for task in tasksToView:
        print(f"{task.id:<5} {task.description:<30} {task.status:<8} {task.getDateString("c"):<20} {task.getDateString("u"):<20}")

def findTask(task_id):
    for task in tasks:
        if task.id == task_id:
            return task
tasks = []



while True:
    tokens = input("> ").split()
    if len(tokens) == 0:
        print("Invalid input!")
        continue
    try:
        if tokens[0] == "add":
            tasks.append(Task(tokens[1]))
        elif tokens[0] == "list":
            if len(tokens) > 1:
                listTasks(tokens[1])
            else:
                listTasks("all")
        elif tokens[0] == "delete":
            deleteTask(tokens[1])
        elif tokens[0] == "mark-in-progress":
            findTask(tokens[1]).updateStatus("in-progress")
        elif tokens[0] == "mark-done":
            findTask(tokens[1]).updateStatus("done")
        elif tokens[0] == "update":
            findTask(tokens[1]).updateDescription(tokens[2])
        elif tokens[0] == "exit":
            saveTasks()
            print("Saving and Exiting...")
            break
        else:
            print("Invalid input!")
    except IndexError:
        print("Error: Command takes more inputs!")
    except Exception:
        print("Error: list accepts optional arguments: (done/todo/in-progress)")
    
