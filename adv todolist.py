# Python Project 1: Advanced To-Do List Application

# Name: Nazish Ajaz

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Complete")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Add Task
    if choice == "1":

        task = input("Enter task: ").strip()

        if task == "":
            print("Task cannot be empty.")

        elif task.isdigit():
            print("Please enter a valid task name.")

        elif any(t["name"] == task for t in tasks):
            print("Task already exists.")

        else:
            tasks.append({
                "name": task,
                "done": False
            })

            print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if not tasks:
            print("\nNo tasks available.")

        else:
            print("\n===== YOUR TASKS =====")

            for i, task in enumerate(tasks, start=1):

                status = "✓" if task["done"] else " "

                print(f"{i}. [{status}] {task['name']}")

        input("\nPress Enter to return to the menu...")

    # Delete Task
    elif choice == "3":

        if not tasks:
            print("\nNo tasks available to delete.")

        else:
            print("\n===== YOUR TASKS =====")

            for i, task in enumerate(tasks, start=1):

                status = "✓" if task["done"] else " "

                print(f"{i}. [{status}] {task['name']}")

            try:
                task_num = int(input("\nEnter task number to delete: "))

                if 1 <= task_num <= len(tasks):

                    removed_task = tasks.pop(task_num - 1)

                    print(f"'{removed_task['name']}' deleted successfully!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Mark Complete
    elif choice == "4":

        if not tasks:
            print("\nNo tasks available.")

        else:
            print("\n===== YOUR TASKS =====")

            for i, task in enumerate(tasks, start=1):

                status = "✓" if task["done"] else " "

                print(f"{i}. [{status}] {task['name']}")

            try:
                task_num = int(input("\nEnter task number to mark complete: "))

                if 1 <= task_num <= len(tasks):
                    if tasks[task_num - 1]["done"]:
                        print("Task is already completed.")
                    else:
                        tasks[task_num - 1]["done"] = True
                        print("Task marked as completed!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
         print("Thank you for using the To-Do List App!")
         break

    else:
        print("Invalid choice. Try again.")