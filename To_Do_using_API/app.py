from delete_todos import delete_todos
from get_todos import fetch_todos, print_todos, fetch_todos_by_id
from post_todos import post_todos
from patch_todos import patch_todos


#universal url
url = "https://api.freeapi.app/api/v1/todos"

def main():
    print("-"*50)
    print("Welcome to the Todo App")
    while True:
        print("Choose an option: ")
        print("1. Fetch Todos")
        print("2. Add Todo")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                todos, message = fetch_todos()
                if todos:
                    print_todos(todos)
                    print(message)
                else:
                    print(message)
            case "2":
                title = input("Enter the title: ")
                description = input("Enter the description: ")
                todo, message = post_todos(title, description)
                if todo:
                    print(f"Todo added with id: {todo['_id']}")
                    print(message)
                else:
                    print(message)
            case "3":
                print_todos(fetch_todos()[0])
                id = input("Enter the id of the todo: ")
                title = input("Enter the title: ")
                description = input("Enter the description: ")
                todo, message = patch_todos(id, title, description)
                if todo:
                    print(f"Todo updated with id: {todo['_id']}")
                    print(message)
                else:
                    print(message)

            case "4":
                print_todos(fetch_todos()[0])
                id = input("Enter the id of the todo: ")
                message = delete_todos(id)
                if message:
                    print(f"Todo deleted with id: {id}")
                    print(message)
                else:
                    print(message)
            case "5":
                print("Thank you for using the Todo App")
                print("-"*50)
                break
            case _:
                print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
