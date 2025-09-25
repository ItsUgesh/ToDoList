tasks = []


def list_tasks():
    if not tasks:
        print("There are currently no tasks available.")
    else:
        print("Current tasks")
        for index, task in enumerate(tasks, start= 1):
            print(f"Task #{index}. {task}")


def add_task():
    task = input("Add a task: ")
    tasks.append(task)
    print(f"Task '{task}' is added to the list")


def delete_task():

    list_tasks()
    try:
        task_to_delete = int(input("Enter the number of task to delete: "))
        index = task_to_delete - 1
        if index >= 0 and index < len(tasks):
            tasks.pop(index)
            print(f"Task {task_to_delete} has been deleted")
        else:
            print(f"Task {task_to_delete} was not found")

    except:
        print("Invalid Input")


if __name__ == "__main__":
    # loop to run the app
    print(" ")
    print("Welcome to your to do list.")

while True:
    print("")
    print("Select from the list")
    print("--------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List your tasks")
    print("4. Quit")

    choice = input("Choose your wish => ")
    if (choice == "1"):
        add_task()
    elif (choice == "2"):
        delete_task()
    elif (choice == "3"):
        list_tasks()
    elif (choice == "4"):
        break
    else:
        print("Invalid input. Please try again")


print("SAYONARA")
