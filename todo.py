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
