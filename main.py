from json import loads, dumps

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    

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

