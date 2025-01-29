# To do list

tasks = [] # list

def display_menu():
    print("\nWelcome to your To-Do List App")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    task = input("Enter Task title: ")
    tasks.append({"title": task, "status": "Incomplete"})
    print("Task added succesfully!")

def view_tasks():
    try:
        if not tasks:
            print("You have no tasks.")
        else:
            print("Current tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['title']} - {task['status']}")
    except Exception as e:
        print(f"Error in view_tasks(): {e}")

def mark_complete():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Complete"
            print("Task marked as complete!")
            remaining_tasks = sum(1 for task in tasks if task["status"] == "Incomplete")
            print(f"You have {remaining_tasks} remaining task(s) to complete.")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            print("The task has been deleted.")
            remaining_tasks = sum(1 for task in tasks if task["status"] == "Incomplete")
            print(f"You have {remaining_tasks} remaining task(s) to complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = input("Choose an option: ")
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                mark_complete()
            elif choice == '4':
                delete_task()
            elif choice == '5':
                print("Thank you for using the App!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"Am error occurred: {e}")
        finally:
            print("\nReturning to menu....")

if __name__ == "__main__":
    main()


