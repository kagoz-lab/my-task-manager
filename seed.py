from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from todo import Base, Task  # Import the Task model

# Database setup
DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables if they don't exist

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Seed data
def seed_data():
    tasks = [
        Task(title="Task 1", description="Description for Task 1", priority="high", due_date=datetime.strptime("2023-12-31", "%Y-%m-%d").date()),
        Task(title="Task 2", description="Description for Task 2", priority="medium", due_date=datetime.strptime("2023-11-30", "%Y-%m-%d").date()),
        Task(title="Task 3", description="Description for Task 3", priority="low", due_date=datetime.strptime("2023-10-31", "%Y-%m-%d").date()),
    ]
    
    session.add_all(tasks)  # Add all tasks to the session
    session.commit()  # Commit the changes
    print("Seed data added successfully!")

if __name__ == "__main__":
    seed_data()
