from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
tasks_collection = db.tasks


# Insert Function
def create_task(description):
    task = {
        'task': description
    }

    result = tasks_collection.insert_one(task)
    print(f'Task Created with id {result.inserted_id}')


# View Function
def view_tasks():
    tasks = tasks_collection.find()

    print("\n--- Tasks ---")

    for task in tasks:
        print(task)

#Read Function
def read_tasks():
    tasks = tasks_collection.find()
    for docs in tasks:
        print(f"{docs['task']}")


while True:
    print("\n1. Create Task")
    print("2. View Task")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        description = input("Enter your Task: ")
        create_task(description)   

    elif choice == '2':
        read_tasks()

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Provide VALID INPUT")