from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
tasks_collection = db.tasks


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_task():
    title = input("Enter Task Title: ")
    priority = input("Priority (Low/Medium/High): ")
    category = input("Category: ")
    deadline = input("Deadline (DD-MM-YYYY): ")

    task = {
        'title': title,
        'priority': priority,
        'category': category,
        'deadline': deadline,
        'status': 'Pending',
        'created_at': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        'completed': False,
        'favorite': False
    }

    result = tasks_collection.insert_one(task)
    print(f"\nTask Added Successfully : {result.inserted_id}")



def view_tasks():
    tasks = list(tasks_collection.find())

    if len(tasks) == 0:
        print("\nNo Tasks Found")
        return

    print("\n========= TASKS =========")

    for task in tasks:
        print(f"""
ID        : {task['_id']}
Title     : {task['title']}
Priority  : {task['priority']}
Category  : {task['category']}
Deadline  : {task['deadline']}
Status    : {task['status']}
Favorite  : {task['favorite']}
Created   : {task['created_at']}
""")
        print("Invalid Choice")