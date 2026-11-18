
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n--- YOUR TO-DO LIST ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['name']}")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== PYTHON TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter task: ").strip()
            if name:
                tasks.append({"name": name, "done": False})
                save_tasks(tasks)
                print("Task added successfully!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                number = int(input("Enter task number: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            show_tasks(tasks)
            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    tasks.pop(number - 1)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
