tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
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

    elif choice == "2":
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

    elif choice == "3":
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

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please select an option from 1-4.")