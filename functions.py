FP = "todos.txt"

def get_todos(filename=FP):
    with open(filename, "r") as f:
        file = f.readlines()
        return file
    
def write_todos(todo_list, filename=FP):
    with open(filename, "w") as f:
        f.writelines(todo_list)