# To-Do List

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_no = int(input("Enter task number to remove: "))
            
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(removed, "removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice! Please try again.")
