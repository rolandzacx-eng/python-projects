import json

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added!")

def view_task(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks):
        status = "x" if t["done"] else " "
        print(f"{i+1}. [{status}] {t['task']}")

def mark_done(tasks):
    view_task(tasks)
    if not tasks:
        return
    num = int(input("Which task number is done? ")) - 1
    if 0 <= num < len(tasks):
        tasks[num]["done"] = True
        print("Marked done!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_task(tasks)
    if not tasks:
        return
    num = int(input("Which task number to delete? ")) - 1
    if 0 <= num < len(tasks):
        removed = tasks.pop(num)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")

def save_tasks(tasks):
    file = open("tasks.json", "w")
    json.dump(tasks, file)
    file.close() 

def load_tasks():
    try:
        file = open("tasks.json", "r")
        tasks = json.load(file)
        file.close()
        return tasks
    except:
        return[]

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
main()
