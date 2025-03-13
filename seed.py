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
        Task(title="Go to the barber", description="Get a haircut and beard trim", priority="high", due_date=datetime.strptime("2023-12-01", "%Y-%m-%d").date()),
        Task(title="Buy groceries", description="Purchase fruits, vegetables, and snacks", priority="medium", due_date=datetime.strptime("2023-11-15", "%Y-%m-%d").date()),
        Task(title="Finish the project report", description="Complete the final report for the project", priority="low", due_date=datetime.strptime("2023-11-30", "%Y-%m-%d").date()),
    ]
    
    session.add_all(tasks)  # Add all tasks to the session
    session.commit()  # Commit the changes
    print("Seed data added successfully!")

if __name__ == "__main__":
    seed_data()
