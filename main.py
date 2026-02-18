from json import loads, load, dumps, dump
from datetime import datetime

class Task:
    num = 0
    def __init__(self, description):
        Task.num += 1
        self.id = Task.num
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now()
        self.updatedAt = "N/A"

    def updateDescription(self, description):
        self.description = description
        self.updatedAt = datetime.now()

    def updateStatus(self, status):
        self.status = status
        self.updatedAt = datetime.now()

    def getDateString(self, type):
        if type == "c":
            if len(str(self.createdAt)) > 20:
                return str(self.createdAt)[:-10]
            else:
                return str(self.createdAt)[:-3]
        elif type == "u":
            if len(str(self.updatedAt)) > 20:
                return str(self.updatedAt)[:-10] if self.updatedAt != "N/A" else "N/A"
            else:
                return str(self.updatedAt)[:-3] if self.updatedAt != "N/A" else "N/A"
    
tasks = []
    

def convert_to_json(task):
    dic = {
        "id": task.id,
        "description": task.description,
        "status": task.status,
        "createdAt": task.getDateString("c"),
        "updatedAt": task.getDateString("u")
    }
    return dumps(dic)

def convert_to_task(dic):
    task = Task(dic["description"])
    task.id = dic["id"]
    task.status = dic["status"]
    task.createdAt = datetime.strptime(dic["createdAt"], "%Y-%m-%d %H:%M")
    task.updatedAt = datetime.strptime(dic["updatedAt"], "%Y-%m-%d %H:%M") if dic["updatedAt"] != "N/A" else "N/A"

    return task


def saveTasks():
    tasksD = list(map(convert_to_json, tasks))
    with open("tasks.json", "w") as tasksFile:
        dump(tasksD, tasksFile)

def loadTasks():
    global tasks
    with open("tasks.json", "r") as tasksFile:
        if len(tasksFile.read(5)) <= 2:
            return
        tasksFile.seek(0)
        jsonList = load(tasksFile) #TODO: Fix bug with loading not working
    
    tasks = [convert_to_task(loads(jsonTask)) for jsonTask in jsonList]


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
        raise LookupError
    if not tasksToView:
        print("No tasks yet")
        return
    print("="*96)
    print(f"{"ID":<5} {"Description":<30} {"Status":<12} {"Created At":<20} {"Updated At":<20}")
    for task in tasksToView:
        print(f"{task.id:<5} {task.description:<30} {task.status:<12} {task.getDateString("c"):<20} {task.getDateString("u"):<20}")

def findTask(task_id):
    task_id = int(task_id)
    for task in tasks:
        if task.id == task_id:
            return task
    raise NameError

loadTasks()

while True:
    tokens = input("> ").split()
    if len(tokens) == 0:
        print("Invalid input!")
        continue
    try:
        if tokens[0] == "add":
            task_to_add = Task(" ".join(tokens[1:]).strip('"'))
            tasks.append(task_to_add)
            print(f"Task added successfully (ID: {task_to_add.id})")
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
            findTask(tokens[1]).updateDescription(" ".join(tokens[2:]).strip('"'))
        elif tokens[0] == "exit":
            saveTasks()
            print("Saving and Exiting...")
            break
        else:
            print("Invalid input!")
        saveTasks()
    except IndexError:
        print("Error: Command takes more inputs!")
    except LookupError:
        print("Error: list accepts optional arguments: (done/todo/in-progress)")
    except NameError:
        print("Error: Task with given ID does not exist!")
    except ValueError:
        print("Error: ID should be a number!")
    
