from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base  # Updated import
from datetime import datetime  # Import datetime for date validation

# Database setup
DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the Task model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    priority = Column(String, nullable=False)  # New column for task priority
    due_date = Column(Date, nullable=False)    # New column for task due date

# Create the database and tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# CLI Menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    priority = input("Enter task priority (low, medium, high): ")  # New input for priority
    while priority not in ["low", "medium", "high"]:
        print("Invalid priority. Please enter 'low', 'medium', or 'high'.")
        priority = input("Enter task priority (low, medium, high): ")
    
    due_date = input("Enter task due date (YYYY-MM-DD): ")  # New input for due date
    while True:
        try:
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d').date()  # Convert to date object
            break
        except ValueError:
            print("Invalid date format. Please enter the date in 'YYYY-MM-DD' format.")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
    
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")

    task = Task(title=title, description=description, priority=priority, due_date=due_date_obj)  # Use date object
    session.add(task)
    session.commit()
    print("Task added successfully!")

def view_all_tasks(): 
    filter_choice = input("Filter by (1) Completed (2) Pending (3) All: ")  # New filter option
    if filter_choice == "1":
        tasks = session.query(Task).filter_by(completed=True).all()
    elif filter_choice == "2":
        tasks = session.query(Task).filter_by(completed=False).all()
    else:
        tasks = session.query(Task).all()
    
    if not tasks:
        print("No tasks found.")
    else:
        print("\nAll Tasks:")
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.id}. {task.title} - {task.description} [{status}]")

def mark_task_completed():
    task_id = int(input("Enter the task ID to mark as completed: "))
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = True
        session.commit()
        print(f"Task '{task.title}' marked as completed!")
    else:
        print("Task not found.")

def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    confirm = input(f"Are you sure you want to delete task ID {task_id}? (yes/no): ")
    if confirm.lower() not in ['yes', 'y']:
        print("Task deletion cancelled.")
        return
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' deleted successfully!")
    else:
        print("Task not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
