from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TestMigration(Base):
    __tablename__ = 'test_migration'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Define the engine
DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(DATABASE_URL)

def upgrade():
    # Create the test_migration table
    Base.metadata.create_all(bind=engine)

def downgrade():
    # Drop the test_migration table
    Base.metadata.drop_all(bind=engine)
