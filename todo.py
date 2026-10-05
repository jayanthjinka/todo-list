tasks = []

description = input("Enter a task: ")

if description == "":
    print("Task description cannot be empty.")
else:
    task = {
        "description": description,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")

print("\nTasks:")

if len(tasks) == 0:
    print("No tasks found.")
else:
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{index}. {task['description']} - {status}")

try:
    choice = int(input("Enter task number: "))

    if choice < 1 or choice > len(tasks):
        print("Invalid task number.")
    else:
        index = choice - 1
        tasks[index]["completed"] = True
        print("Task marked as completed.")

except ValueError:
    print("Please enter a valid number.")
