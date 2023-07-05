tasks = []

def add_task():
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
   if len(tasks) == 0:
       print("No tasks to remove")
   else:
       print("Current Tasks:")
       display_tasks()
       index = int(input("enter the index to remove"))
       if index < 0 or index >= len(tasks):
           print("invalid index")
       else:
           removed_task = tasks.pop(index)
           print("Task Removed:",removed_task)
def display_tasks():
    if len(tasks) == 0:
        print("No Tasks assigned")
    else:
        for i,task in enumerate(tasks):
            print(f"{i}.{task}")

# Main program loop
while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")
