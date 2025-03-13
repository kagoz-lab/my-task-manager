from logging.config import fileConfig
import sys
import os
from datetime import datetime  # Import datetime for date validation
from sqlalchemy import engine_from_config  # Import engine_from_config
from sqlalchemy import pool
from alembic import context  # Import context
from alembic.config import Config  # Import Config class
from todo import Base  # Use absolute import

# Add the current directory to the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Instantiate the config object
config = Config("alembic.ini")

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
