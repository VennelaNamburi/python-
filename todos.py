import json
with open("C:\\Users\\venne\\Documents\\todos.json","r") as j:
    Todolist='{"task1":"doing yoga","task2":"go to supermarket"}'
    add_todo={"task3":"study"}
    json.loads(j.read())
    data=json.loads(Todolist)
    data.update(add_todo)
    if 'task1' in data:
        del data['task1']
    print(data)
